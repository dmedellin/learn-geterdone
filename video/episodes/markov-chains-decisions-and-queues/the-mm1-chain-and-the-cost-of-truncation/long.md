---
format: long
lesson: markov-chains-decisions-and-queues/the-mm1-chain-and-the-cost-of-truncation
title: The M/M/1 queue from the cut equation, and the cost of truncating it
thumb: Print the missing tail
---

@chapter Constant rates
@title text="The M/M/1 Chain and the Cost of Truncation" sub="Markov Chains, Decisions and Queues" art=thumb
The simplest queue has one server, arrivals at a steady rate, and service at a steady rate. Feed those into the cut equation and the famous geometric distribution falls straight out.

@art constant-rates
In the M M one chain, the arrival rate is lambda in every state, and the service rate is mu in every state above zero. Write rho for lambda over mu, the utilisation.

@art rate-vs-time
One warning first. Mu is a rate, not a time. A service taking a fifth of a unit of time has mu equals five. Enter a fifth instead against lambda of four, and you report rho of twenty, an overloaded system, when it's really four fifths loaded.

@chapter Geometric, derived
@math heading="Every cut gives ρ" items="πₙ₊₁ = πₙ · λ/μ = πₙ·ρ@every cut;;πₙ = π₀ ρⁿ@by induction;;π₀ = 1 − ρ,  L = ρ/(1 − ρ)@one minus rho;;P(N > k) = ρ^(k+1)@more than k"
Every cut gives the same ratio, rho, so pi n is pi zero times rho to the n, by induction. For rho below one, pi zero is one minus rho, and the mean L is rho over one minus rho. The chance of more than k in the system is rho to the k plus one.

@art geometric-bars
So the geometric shape isn't assumed. It's a consequence of one equation, applied over and over. And if rho is one or more, the weights never sum to anything finite, so there's no distribution at all.

@chapter What truncation costs
@art cut-tail
But the lab works on a finite chain, and an M M one queue has infinitely many states. So every figure is an approximation. The untruncated chain puts exactly rho to the N plus one above state N, and the finite chain spreads that over the states it kept.

@math heading="ρ = 4/5, kept to state 40" items="L:  3.99564 vs 4@three point nine nine;;tail lost:  ρ⁴¹ ≈ 0.000106@one part;;π₀ ≈ 0.2000212699 vs 1/5@pi zero"
With lambda four and mu five, rho is four fifths. Keep forty states and the chain's L is about three point nine nine five six, against the closed form's four. The lost tail is about one part in ten thousand. And pi zero is a touch above a fifth, because state zero gets the biggest share of the redistributed tail.

@art heavy-tail
Now nineteen twentieths loaded, kept to sixty states. The lost tail is about four point four percent, and the chain's L is about sixteen point two, against nineteen. That mass sits at large n, so the mean is very sensitive to it.

@words text="Exact, about a different question" sub="π₀: 28 digits over 29"
That isn't arithmetic error. Pi zero is an exact fraction, twenty eight digits over twenty nine. It's the exact answer to a slightly different question, a chain with a ceiling.

@chapter The light-load trap
@art light-tail
At half loaded, with thirty states, rho to the thirty one is about five times ten to the minus ten. L is nought point nine nine nine nine nine nine nine nine, against one. Negligible. This is the case people generalise from, and that's the mistake.

@words text="Tail mass falls like ρᴺ"
Halving the load doesn't halve the error, it changes its exponent. At nineteen twentieths, the same thirty states would be useless. So the page prints the lost mass, and you never have to guess which case you're in.

@chapter When ρ ≥ 1
@words text="λ = 5 · μ = 4 · ρ = 5/4" sub="no M/M/1 distribution"
Set lambda five and mu four. Now there's no M M one queue at all: the backlog grows forever. The finite chain still has a distribution, but it's a buffered model, and reporting it as M M one would be a number for a queue that has none.

@chapter Where people slip
@list heading="Common slips" items="Reporting finite-chain figures as M/M/1@The first|Generalising from light load@The second|Entering a service time as μ@And the third"
The first slip is reporting a finite chain's figures as M M one figures. The second is generalising from a lightly loaded example. And the third is entering the service time where the rate belongs.

@chapter Try it
@words text="ρ = 19/20" sub="how many states until the lost tail is below 1%?"
Your turn. At nineteen twentieths loaded, the lost tail is rho to the N plus one. Find the smallest number of states that keeps it below one percent, and compare that with the forty that was plenty at four fifths.

@end text="Print the tail you dropped"
You can slide the load and the number of states and watch the two L columns separate, on Learn. That's learn dot get er done dot I O.
