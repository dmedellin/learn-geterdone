---
format: long
lesson: markov-chains-decisions-and-queues/the-cut-equation-and-every-queue-from-it
title: The cut equation: one idea that solves every birth-death queue
thumb: Up must equal down
---

@chapter A queue is a chain
@title text="The Cut Equation, and Every Queue From It" sub="Markov Chains, Decisions and Queues" art=thumb
A queue looks complicated. But as a chain it's simple: the number in the system goes up by one, or down by one, and that's all. That one fact solves almost everything.

@art birth-death-line
That's a birth death chain. States zero to N. From state n, it moves up at rate lambda n, an arrival, and down at rate mu n, a service. There's no arrival out of the top, and no service out of zero.

@chapter The cut
@art cut-line
Draw a line between n and n plus one. In the long run, the chain crosses it upward exactly as often as it crosses back down.

@art alternating-crossings
Why? It moves one step at a time, so it can't cross up twice in a row without being on both sides at once. The crossings alternate, so the two counts differ by at most one.

@math heading="The cut equation" items="πₙ λₙ = πₙ₊₁ μₙ₊₁@pi n;;πₙ₊₁ = πₙ · λₙ / μₙ₊₁@so pi n plus one"
The rate up is pi n times lambda n. The rate down is pi n plus one times mu n plus one. They're equal. So pi n plus one is pi n times lambda n over mu n plus one.

@words text="No assumption about the rates"
Notice what the argument didn't assume. Not constant rates, not an infinite chain, not stability. So one equation serves every model.

@chapter Three machines, one repairer
@art repair-shop
Here's the lesson's example. Three machines, each failing at rate one, so the failure rate is three, then two, then one, as fewer are left to fail. One repairer, working at rate two.

@math heading="Chain the ratios" items="cut 0|1:  × 3/2@three halves;;cut 1|2:  × 1@one;;cut 2|3:  × 1/2@a half;;1 + 3/2 + 3/2 + 3/4 = 19/4@nineteen quarters;;π = (4/19, 6/19, 6/19, 3/19)@Divide, and pi"
The first cut's ratio is three halves. The second is one. The third is a half. So the running product is one, three halves, three halves, three quarters, which adds to nineteen quarters. Divide, and pi is four, six, six and three nineteenths.

@art ratio-chain
No matrix anywhere. Each state's probability is the one before it, times a ratio.

@chapter Check it another way
@art two-routes-agree
Because the cut is the step you're asked to believe, the page also builds the full balance system, drops one equation, adds the sum to one, and eliminates. Fifteen operations. It gives four, six, six and three nineteenths, identical, fraction by fraction.

@math heading="The full balance system" items="πₙ(λₙ + μₙ) = πₙ₋₁λₙ₋₁ + πₙ₊₁μₙ₊₁@flow out"
Each of those equations says flow out of a state equals flow in: pi n times lambda n plus mu n, equals the flow up from below plus the flow down from above. The two routes share no arithmetic at all, and the page compares them as exact fractions, not as decimals that look alike.

@chapter Little's law, with the right rate
@math heading="The rate that gets in" items="L = Σ n·πₙ = 27/19@twenty seven;;λ_eff = 3·4/19 + 2·6/19 + 1·6/19 = 30/19@thirty nineteenths;;W = L / λ_eff = 9/10@nine tenths"
The mean number in the system, L, is twenty seven nineteenths. To get the time, divide by the rate that actually gets in, the admitted rate. That's thirty nineteenths here. So W is nine tenths. Dividing by the raw arrival rate would credit the shop with failures that never happen.

@chapter Two servers, and too fast
@words text="λ = 4, 4, 4, 4, 4 · μ = 3, 6, 6, 6, 6" sub="π = (243, 324, 216, 144, 96, 64) / 1087"
Two servers is just one changed list. Arrivals at four, service at three from state one, then six. Ratios four thirds, then two thirds. Now the most likely state is one, not zero, and no formula was needed to see it.

@words text="λ = 5 · μ = 3" sub="π = (81, 135, 225, 375, 625) / 1441"
And if arrivals beat service, five against three, the mass piles up at the top. That's an answer about this finite chain. The unbounded queue would have no distribution at all.

@chapter Where people slip
@list heading="Common slips" items="Lining the rate lists up wrong@The first|Dividing L by λ, not λ_eff@The second|Thinking the cut is an M/M/1 trick@And the third"
The first slip is lining the rate lists up wrong, which gives a perfectly normalised answer for the wrong chain. The second is dividing L by lambda when arrivals depend on the state. And the third is thinking the cut is a special trick. It's the general statement.

@chapter Try it
@words text="Drop a different equation" sub="λ = 3, 2, 1 · μ = 2, 2, 2"
Your turn. Build the full balance system for the repair shop and drop a different equation than the page did. Solve it exactly. You should still get four, six, six and three nineteenths.

@end text="Cut the chain, chain the ratios"
You can type your own arrival and service rates and see every cut, on Learn. That's learn dot get er done dot I O.
