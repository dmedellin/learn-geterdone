---
format: long
lesson: queues-and-utilisation/bounded-queues-and-loss
title: Bounded queues and loss: trading waiting for dropping
thumb: Drop, or delay?
---

@chapter The question
@title text="Bounded Queues and Loss" sub="Queues and Utilisation" art=thumb
Give a queue a limit of K, and arrivals that find it full are refused. The system stops trading latency for completeness and starts trading completeness for latency. How much does it drop, and what does that do to your numbers?

@art bounded-buffer
M M one K is the M M one model with room for at most K in the system, the one in service included. An arrival that finds K present is blocked and lost. The states zero to K keep the same geometric ratios as before, normalised over a finite sum.

@math heading="Blocking probability" items="π_K = (1 − ρ)ρᴷ / (1 − ρᴷ⁺¹)@the fraction of time"
The fraction of time the system is full is one minus rho, times rho to the K, over one minus rho to the K plus one.

@words text="time full = arrivals blocked, because arrivals are Poisson" sub="PASTA: Poisson arrivals see time averages"
That's the fraction of time. The loss is the fraction of arrivals that find it full. They're equal here only because arrivals are Poisson, and a Poisson arrival sees the system the way a random outside glance would. That's called PASTA, and it's an assumption of this model, not a general truth.

@chapter A worked example
@math heading="λ = 4/5,  μ = 1,  K = 4" items="π_K = 256/2101 ≈ 12.2%@two hundred and fifty six;;λ_eff = λ(1 − π_K) = 1476/2101 ≈ 0.703/s@the admitted rate;;L = 3284/2101 ≈ 1.563@the mean number"
At lambda four fifths, mu one, and room for four, the blocking probability is two hundred and fifty six over twenty one oh one, about twelve point two percent. So the admitted rate is lambda times one minus that, about nought point seven nought three a second. And the mean number in the system is about one point five six three.

@math heading="Little's Law takes the admitted rate" items="W = L/λ_eff = 821/369 ≈ 2.22 s  ✓@admitted rate;;W = L/λ ≈ 1.95 s  ✗@the offered rate"
Little's Law was proved by counting customers who actually entered. So divide by the admitted rate, and W is about two point two two seconds. Divide by the offered rate instead and you get one point nine five, twelve percent low.

@art boundary-crossing
And it's low in the flattering direction. That's a response time no admitted request experiences, on a system also dropping about one arrival in eight. A dropped arrival never crossed the boundary, so it belongs in neither lambda nor W.

@chapter It always settles
@art uniform-states
This chain settles at every rho, even at one or more. There are finitely many states, and the queue can't grow past K. At rho of one, every state is equally likely, so with K of four the blocking is exactly one fifth. Overload in a bounded system isn't unbounded growth. It's loss.

@chapter Sizing the buffer
@math heading="λ = 4/5,  μ = 1,  S = 1 s" items="K = 4:  loss ≈ 12.2%,  cap ≈ 4 s@K of four;;K = 14:  loss ≤ 1%,  cap ≈ 14 s@fourteen;;K = 24:  loss ≤ 0.1%,  cap ≈ 24 s@twenty four"
At most K jobs can be ahead of you, so the wait can't exceed roughly K times S. With K of four, loss is twelve point two percent and the cap about four seconds. At fourteen, loss is at most one percent, cap fourteen seconds. At twenty four, at most a tenth of a percent, cap twenty four seconds.

@art bufferbloat
That's bufferbloat in four lines. Pushing loss from twelve percent to a tenth of a percent costs a latency cap of twenty four service times. A queue that deep delivers answers that stopped being wanted long ago.

@art short-vs-deep
So the question is never how to stop dropping. It's which failure is cheaper for this request. For an interactive request with a client timeout, delay past the timeout is loss with extra steps. A short buffer refuses early enough for the client to react. For a batch pipeline with no one waiting, a deep buffer is exactly right.

@chapter Where people slip
@list heading="Common slips" items="Little's Law with the offered rate@The first|A bigger buffer is always better@The second|Thinking it needs ρ < 1 to settle@The third"
The first slip is using Little's Law with the offered rate. The wrong answer is the smaller one, which is why it survives review. The second is believing a bigger buffer is always better. And the third is assuming the queue needs rho below one to settle.

@chapter Try it
@words text="λ = 4/5 · μ = 1 · K = 2" sub="π_K will be much larger than 12%"
Your turn. Keep lambda four fifths and mu one, but set K to two. The blocking probability will be much larger than twelve percent, so the admitted rate falls further from the offered one. Compute both W values, and the factor between them.

@end text="Little's Law takes the admitted rate"
You can set the load and the buffer size and see loss, latency cap and both W values, on Learn. That's learn dot get er done dot I O.
