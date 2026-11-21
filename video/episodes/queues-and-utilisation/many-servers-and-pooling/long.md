---
format: long
lesson: queues-and-utilisation/many-servers-and-pooling
title: Many servers: why one shared queue beats four
thumb: Same servers, 53/9 less waiting
---

@chapter The question
@title text="Many Servers: Pooling, and Erlang C" sub="Queues and Utilisation" art=thumb
Four servers, the same load. You can give each server its own queue and split the traffic evenly, or put one queue in front of all four. The utilisation is identical either way. The waiting is not, by nearly six times.

@art separate-vs-pooled
The whole mechanism is one sentence. A separate queue can be idle while another waits. Sooner or later, one server has nothing to do while somebody waits in another line, and every such moment is capacity you paid for and didn't use. One shared queue makes that state impossible.

@chapter Offered load
@art four-servers
Same machines, same work, same fraction of time busy. This isn't a comparison between a busy system and a quiet one.

@math heading="M/M/s" items="a = λ/μ@offered load;;ρ = a/s@per server;;settles when ρ < 1@settles"
M M s is the M M one model with s identical servers behind one queue. The offered load a is lambda over mu, measured in servers: how many servers the work would keep permanently busy. The utilisation per server is a over s, and the system settles when that's below one.

@words text="C(s, a): the chance an arrival waits at all" sub="Erlang C, stated here, derived in Operations Research"
Erlang C gives the probability that an arrival has to wait at all. Its derivation lives in Operations Research. Here we use it as an instrument. From it, L q is C times rho over one minus rho, and W q comes from Little's Law. At s equals one, it collapses to the single server results.

@chapter A worked example
@math heading="λ = 3,  μ = 1,  s = 4" items="a = 3,  ρ = 3/4@three servers' worth;;C(4, 3) = 27/53 ≈ 0.5094@twenty seven over fifty three;;L_q = (27/53)(3) = 81/53@eighty one;;W_q = L_q/λ = 27/53 s ≈ 0.51 s@the pooled wait"
Take lambda three, mu one, and four servers. That's three servers' worth of work, so rho is three quarters. The chance of waiting at all is twenty seven over fifty three. L q is that times three, eighty one over fifty three. And the pooled wait is twenty seven over fifty three of a second, about half a second.

@math heading="Four separate queues, λ/4 each" items="ρ = 3/4 each@three quarters each;;L_q = ρ²/(1 − ρ) = 9/4@nine quarters;;W_q = (9/4)/(3/4) = 3 s@three seconds;;3 ÷ 27/53 = 53/9 ≈ 5.9@fifty three ninths"
Now split the traffic: each server gets three quarters a second, so rho is three quarters each, the same. Each queue holds nine quarters waiting, and waits three seconds. Three seconds against twenty seven fifty thirds is fifty three ninths, nearly six times.

@art idle-while-waiting
The split system isn't overloaded and isn't misconfigured. It's simply wasting the moments when one of its servers is free and one of its queues isn't. And a perfectly even split still has those moments, because arrivals are random.

@chapter How it moves with load
@list heading="Pooled against separate" items="ρ = 1/2:  2/23 s vs 1 s,  ratio 23/2@a half|ρ = 3/4:  27/53 s vs 3 s,  ratio 53/9@three quarters|ρ = 9/10:  4374/2221 s vs 9 s,  ratio ≈ 4.6@nine tenths"
At rho of a half, the pooled queue waits two twenty thirds of a second against one, a ratio of twenty three halves, but a saving under a second. At three quarters, the ratio is fifty three ninths and the saving about two and a half seconds. At nine tenths, the ratio is about four point six, and the saving about seven seconds.

@art seconds-vs-ratio
So pooling matters most under load is true of the seconds and false of the ratio. And it's the seconds that show up in an incident.

@chapter What pooling costs
@art dispatcher
Pooling isn't free. A shared queue needs a dispatcher, which is a component that can itself queue or fail.

@art pinned-sessions
And work that isn't interchangeable, a pinned session or a warmed cache, loses locality when it's pooled. That shows up as a larger S, which multiplies the whole waiting formula. The gain on queueing has to beat the loss on service.

@chapter Where people slip
@list heading="Common slips" items="An even split is as good as a pool@The first|Comparing at different utilisations@The second|Pooling work that isn't interchangeable@The third"
The first slip is assuming an even split is as good as a pool. It looks the same on a utilisation dashboard. The second is comparing the two arrangements at different utilisations. And the third is pooling work that isn't interchangeable.

@chapter Try it
@words text="μ = 1 · s = 4 · λ = 2" sub="a = 2, ρ = 1/2"
Your turn. Keep mu at one and four servers, and drop the load to two. So a is two and rho is a half. Compute the pooled wait, compare it with the separate one second, and notice the ratio went up while the seconds saved went down.

@end text="One queue, many servers"
You can set the load and the server count and compare pooled and separate waits, on Learn. That's learn dot get er done dot I O.
