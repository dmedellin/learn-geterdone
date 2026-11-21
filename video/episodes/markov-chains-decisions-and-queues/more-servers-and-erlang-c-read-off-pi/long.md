---
format: long
lesson: markov-chains-decisions-and-queues/more-servers-and-erlang-c-read-off-pi
title: More servers and Erlang C, read straight off the chain
thumb: One list changes
---

@chapter One line changes
@title text="More Servers, and Erlang C Read Off π" sub="Markov Chains, Decisions and Queues" art=thumb
Add servers to a queue, and you might expect a whole new theory. You don't need one. One list changes, and the cut equations carry on.

@art servers-fill
With n customers and s servers, the number busy is the smaller of n and s. Below s, every new customer finds a free server. At s and above, every server is busy, and new arrivals wait.

@math heading="The M/M/s chain" items="μₙ = min(n, s)·μ@the smaller"
So the service rate out of state n is the smaller of n and s, times mu, the rate of one server. That's all of it. The cut equations never assumed a constant rate, so they don't notice.

@art rising-rates
Below s, the chain speeds up as it fills. At s and above, it can't speed up any more.

@chapter Two ratios
@math heading="Load and utilisation" items="a = λ/μ@offered load;;ρ = a/s@utilisation"
There are two ratios, and it's easy to use the wrong one. The offered load, a, is lambda over mu: the work arriving, in server loads. The utilisation, rho, is a over s: the share of each server's time. Rho is the one that must be below one.

@chapter Worked example
@words text="λ = 2 · μ = 1 · s = 3" sub="a = 2 · ρ = 2/3"
The lesson's example: arrivals at two, each server at one, and three servers. So the offered load is two, and the utilisation is two thirds.

@math heading="Cut ratios and weights" items="ratios:  2/1, 2/2, 2/3, 2/3, …@two over one;;weights:  1, 2, 2, 4/3, 8/9, …@the weights;;π₀ = 1/9 ≈ 0.111111@pi zero"
The cut ratios are two over one, two over two, then two thirds forever. So the weights are one, two, two, four thirds, eight ninths, and so on. Normalise, and pi zero is a ninth, while pi one and pi two are two ninths each.

@art wait-tail
Now Erlang C. An arrival waits exactly when all servers are busy, when the system is at s or above. So the waiting probability is just pi three plus pi four plus pi five, and on. Added up from the distribution, that's forty four point four four four percent.

@words text="erlangC(2, 1, 3) = 4/9" sub="the closed form agrees"
The closed form for an unbounded queue gives four ninths, the same forty four point four percent. Two different computations, and they agree. Erlang C isn't a second formula here. It's a reading of pi.

@chapter Pooling
@art pooling-collapse
Now keep the offered load at two, and add servers. One server: everyone waits. Two: ninety six point three percent. Three: forty four point four. Four: seventeen point four. Five: under six percent.

@words text="s = 2: ρ = 1" sub="the unbounded queue never settles"
At two servers, rho is exactly one. The work arriving equals the work the servers can do, so the unbounded queue never settles. Any finite queue length there is just the truncation talking.

@art busy-share
And the price of pooling: each server is busy two thirds of the time at three servers, and forty percent at five. Less waiting, more idle servers. A trade, not a free lunch.

@chapter A sentence that needs a condition
@art overload-pile
When the queue settles, the expected number of busy servers equals the offered load. At a of two, it's two at three, four and five servers. But with one server, the busy count is one, not two. The missing work is piling up. So that identity needs rho below one, every time.

@chapter Where people slip
@list heading="Common slips" items="Comparing a with 1, not ρ@The first|Quoting a queue length at ρ = 1@The second|Busy servers = a, whatever s@And the third"
The first slip is comparing the offered load with one instead of the utilisation. The second is quoting a finite queue length at rho equals one. And the third is saying the servers do a's worth of work whatever s is.

@chapter Try it
@words text="λ = 3 · μ = 2 · s = 2" sub="a = 3/2 · ρ = 3/4"
Your turn. Arrivals at three, each server at two, two servers. Find the ratios, weights and waiting probability. You should get about sixty four point three percent.

@words text="Chain 64.285% · closed form 64.286%"
The page's chain and the closed form differ here by about three parts in a million, enough to trip its agreement check. Nothing's wrong: the chain stops at forty states, and the tail decays slowly. A truncated chain is a different model.

@end text="Read Erlang C off the chain"
You can add servers and watch the waiting collapse at a fixed load, on Learn. That's learn dot get er done dot I O.
