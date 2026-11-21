---
format: long
lesson: queues-and-utilisation/sizing-with-littles-law
title: Sizing a connection pool with Little's Law
thumb: 20 connections, not 20 000
---

@chapter The question
@title text="Sizing with Little's Law" sub="Queues and Utilisation" art=thumb
How big should a connection pool be? Nobody chooses the concurrency of a system. It's a throughput times a latency, whether you planned for it or not. So the pool size falls out of one identity.

@art three-forms
Little's Law has three forms, one equation rearranged. L equals lambda W sizes the concurrency. Lambda equals L over W gives the throughput a fixed concurrency supports. And W equals L over lambda gives the time in system the other two imply. Fix any two, and the third follows.

@chapter Sizing a pool
@math heading="500 requests a second at 40 ms" items="W = 40 ms = 0.04 s@forty milliseconds;;L = λW = 500 × 0.04 = 20@twenty;;✗  500 × 40 = 20 000@twenty thousand"
You need five hundred requests a second, and each takes forty milliseconds. Forty milliseconds is nought point nought four seconds. So L is five hundred times nought point nought four, twenty connections in flight. Skip the conversion and you get twenty thousand.

@words text="per second × milliseconds = 1000× too big"
That's the most common arithmetic error on this course. A thousand times too big is large enough to notice, and small enough to be believed once someone has typed it into a configuration file. Convert the latency to seconds first, every time.

@art pool-slots
So on average, twenty connections are busy at any moment. That's not a choice anyone made. It's what five hundred a second at forty milliseconds is.

@art queue-before-pool
Make the pool smaller than that and the concurrency doesn't go down. The excess just turns into queueing in front of the pool, with requests standing in line for a free connection.

@chapter A pool is a ceiling
@math heading="Read it the other way" items="λ = N/W = 20 / 0.04 = 500/s@twenty over"
Now read the identity the other way. N connections, each occupied for W, can start at most N over W pieces of work a second. Twenty over nought point nought four is five hundred a second. No amount of offered load gets more than that through.

@art slower-database
So what happens when the database slows down? The same pool of twenty at eighty milliseconds supports only twenty over nought point nought eight, two hundred and fifty a second. Holding five hundred now needs five hundred times nought point nought eight, forty connections. Nothing about the traffic changed.

@words text="latency regression = throughput regression"
That's why a slower dependency shows up as a throughput incident, not a latency one. The pool was the binding constraint, and N over W moved.

@chapter Threads and cores
@math heading="Work that waits" items="200/s × 0.25 s = 50 in flight@two hundred;;cores: 8@eight cores"
A thread waiting on a network call isn't using a core. Take two hundred requests a second, each spending two hundred and fifty milliseconds mostly waiting on a dependency. That's fifty in flight. Eight cores is the wrong number to compare with. Fifty is the concurrency the work has.

@art waiting-threads
Sizing by core count is right for work that computes and wrong for work that waits. And a database's max connections limit isn't a popularity cap. It's a throughput cap that depends on W, and it changes every time the query mix does.

@chapter Size with headroom
@art bunching
One warning. Sizing a pool at exactly L sizes it at the mean, and the mean isn't the peak. Arrivals bunch. A pool sized at the mean is a queue in front of a queue. And W is exactly what rises when the pool becomes the constraint. Size with headroom, and measure W again afterwards.

@chapter Where people slip
@list heading="Common slips" items="Per second × milliseconds@The first|Sizing waiting threads by cores@The second|Treating the pool size as a guarantee@The third"
The first slip is multiplying a per second rate by a figure in milliseconds. The second is sizing threads by core count when the threads wait. And the third is treating the sized pool as a guarantee, when W can move under it.

@chapter Try it
@words text="2000 requests a second at 5 ms" sub="5 ms = 0.005 s"
Your turn. Size a pool for two thousand requests a second at five milliseconds. Five milliseconds is nought point nought nought five seconds. Then say what ceiling that same pool imposes if the service time doubles. Predict both before you check.

@end text="Convert, then multiply"
You can set the rate and the latency and read the pool size and its ceiling, on Learn. That's learn dot get er done dot I O.
