---
format: long
lesson: queues-and-utilisation/the-mm1-queue
title: The M/M/1 queue, from one balance equation
thumb: Balance across one cut
---

@chapter The question
@title text="The M/M/1 Queue" sub="Queues and Utilisation" art=thumb
One server, memoryless arrivals, memoryless service, room for everyone. How many are in the system on average, and how long does each wait? Every answer comes from one balance equation and a geometric series.

@art single-server
Arrivals are memoryless at rate lambda. Service times are memoryless at rate mu, so the mean service time S is one over mu. There's one server, unlimited room, and customers are taken in order. N is the number in the system, including the one in service. And the model settles exactly when rho, lambda over mu, is below one.

@chapter Balance across a cut
@art cut-between-states
Draw a line between the states with n in the system and those with n plus one. Every crossing upward is an arrival while the system holds n. Every crossing downward is a completion while it holds n plus one. In the long run, the system crosses that line up exactly as often as down.

@math heading="The stationary distribution" items="λπₙ = μπₙ₊₁@lambda pi n;;πₙ₊₁ = ρπₙ  →  πₙ = ρⁿπ₀@rho times;;Σ ρⁿ = 1/(1 − ρ)  →  π₀ = 1 − ρ@sum to one;;πₙ = (1 − ρ)ρⁿ@one minus rho"
So lambda pi n equals mu pi n plus one. Each state is rho times the one before, so pi n is rho to the n times pi zero. The probabilities sum to one, and the geometric series converges exactly when rho is below one, which gives pi zero as one minus rho. So pi n is one minus rho, times rho to the n.

@art decaying-bars
The states decay geometrically. And the condition for the series to converge is the same condition as the queue settling at all.

@chapter Everything else follows
@math heading="The closed forms" items="L = ρ/(1 − ρ)@the mean number;;L_q = ρ²/(1 − ρ)@the number waiting;;W = L/λ = S/(1 − ρ)@Little's Law;;P(N > k) = ρ^(k+1)@the tail"
The mean number in the system, L, is rho over one minus rho. The number waiting, L q, is rho squared over one minus rho. W comes from Little's Law, L over lambda, which simplifies to S over one minus rho. And the tail, the chance of more than k, is rho to the k plus one: the chain climbed k plus one steps, each costing a factor of rho.

@chapter A worked example
@math heading="λ = 4/5,  μ = 1,  ρ = 4/5" items="π₀ = 1/5,  π₂ = 16/125@pi zero;;L = 4,  L_q = 16/5@L is four;;L − L_q = 4/5 = ρ  ✓@the one in service;;W = 5 s,  W_q = 4 s = W − S  ✓@five seconds;;P(N > 3) = ρ⁴ = 256/625 ≈ 0.4096@more than three"
Take lambda four fifths and mu one. Pi zero is a fifth, and pi two is sixteen over a hundred and twenty five. L is four, and L q is sixteen fifths. The difference, four fifths, is rho, the one in service. W is five seconds and W q is four, which differ by S. And the chance of more than three is two hundred and fifty six over six hundred and twenty five.

@art in-service
Those two checks are free. L minus L q must be rho, and W minus W q must be S. If either fails, you've made an arithmetic slip, not a modelling one. And notice L counts the one being served. At four fifths, the system holds four on average, and sixteen fifths of them are queueing.

@chapter Not the slotted simulation
@math heading="Shrinking the slot, ρ/(1 − ρ) = 4" items="Δ = 1:  mean 4/5,  gap 16/5@a slot of one;;Δ = 1/10:  mean 92/25,  gap 8/25@a tenth;;Δ = 1/100:  mean 496/125,  gap 4/125@a hundredth"
It's tempting to say the slotted simulation from earlier confirms these formulas. It doesn't. That's a different chain. Hold lambda and mu fixed, shrink the slot, and its exact mean climbs toward four. At a slot of one the gap is sixteen fifths. At a tenth, eight twenty fifths. At a hundredth, four over a hundred and twenty five.

@art converging-limit
Each gap is exactly a tenth of the one before. The relationship is a limit, linear in delta, not an agreement at any one slot size.

@chapter Four assumptions
@art four-assumptions
Four assumptions are doing the work, and the rest of this course takes each away in turn: memorylessness, the single server, the unlimited room, and the steady state itself.

@chapter Where people slip
@list heading="Common slips" items="Reading L as the number waiting@The first|Calling the simulation a check@The second|Ignoring service variability@The third"
The first slip is reading L as the number waiting. The second is saying this formula is checked against the slotted simulation. And the third is applying it to a service whose variability isn't exponential. Very regular service waits about half what this says, and a heavy tail waits considerably more.

@chapter Try it
@words text="λ = 9/10 · μ = 1" sub="ρ = 9/10, so π₀ = 1/10"
Your turn. Take lambda nine tenths and mu one. Rho is nine tenths, so pi zero is a tenth. Predict L, W and the chance of more than three, then compute them. Notice how much moved for one tenth of extra load.

@end text="One cut, one series"
You can set lambda and mu and read every quantity as an exact fraction, on Learn. That's learn dot get er done dot I O.
