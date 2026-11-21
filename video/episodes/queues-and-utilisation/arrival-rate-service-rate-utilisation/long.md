---
format: long
lesson: queues-and-utilisation/arrival-rate-service-rate-utilisation
title: Lambda, mu and rho: the three symbols of queueing
thumb: μ is a rate, not a time
---

@chapter The question
@title text="λ, μ and ρ" sub="Queues and Utilisation" art=thumb
Eight hundred requests a second arrive at a service that takes one millisecond each. Is it keeping up? You need three symbols to answer, and almost every mistake on this course comes from the middle one.

@art arrivals-and-server
Lambda is how fast work arrives: the mean number of arrivals per unit time. S is the mean service time, how long one server takes over one job. And mu, the service rate, is how many jobs that server can finish per unit time when it never waits for work.

@words text="μ = 1/S" sub="a rate, not a duration"
Mu is one over S. Lambda and mu are rates. S is a duration. You're usually handed a rate from a dashboard and a duration from a trace, and you can't divide them until one has been turned into the other's kind.

@chapter Utilisation
@math heading="800 requests a second, 1 ms service" items="S = 1 ms = 1/1000 s@one millisecond;;μ = 1/S = 1000/s@a thousand;;ρ = λ/μ = 800/1000 = 4/5@four fifths;;1 − ρ = 1/5@a fifth"
One millisecond is a thousandth of a second, so mu is a thousand per second. Rho, the utilisation, is lambda over mu: eight hundred over a thousand, four fifths. The server is busy four seconds in every five. And one minus rho, a fifth, is the headroom a burst lands in.

@art busy-idle
Rho is a rate divided by a rate, so the seconds cancel and it's a pure number: the fraction of time one server is busy. Rho of four fifths says the work offered would keep four fifths of one server occupied. It's not running at eight hundred, and it's not eight hundred times too slow.

@chapter Twice as slow
@math heading="Same load, 2 ms service" items="S = 2 ms → μ = 500/s@two millisecond;;ρ = 800/500 = 8/5@eight fifths;;8/5 ≥ 1: nothing settles@nothing settles"
Now send the same eight hundred a second into a two millisecond service. Mu halves to five hundred, and rho doubles to eight fifths. The load didn't change. The service time did, and that was enough to put the system above one. At eight fifths, nothing settles.

@art slower-dependency
That's the cheapest sensitivity on the course, and the one most often missed. A slower dependency, a larger payload, a colder cache. Each moves mu, and so moves rho, without the traffic changing at all.

@chapter Above one
@art growing-line
At rho of one or more, work arrives at least as fast as it can be finished. There's no long run average queue at all. The backlog grows at lambda minus mu per second, for as long as the condition lasts. That's a straight line, not a queue.

@math heading="λ = 1200/s,  μ = 1000/s" items="λ − μ = 200/s@two hundred;;after one minute: 200 × 60 = 12 000@one minute;;after one hour: 200 × 3600 = 720 000@one hour"
Take twelve hundred a second into a service with mu of a thousand. The backlog grows by two hundred a second. After one minute, twelve thousand are waiting. After one hour, seven hundred and twenty thousand.

@words text="ρ/(1 − ρ) at ρ = 8/5 gives −8/3"
And if you plug rho of eight fifths into a queue formula like rho over one minus rho, you get minus eight thirds. A negative queue is the formula telling you its assumption has failed. Quote the growth rate instead.

@chapter Below one
@art rho-dial
Below one, the queue does settle, and the rest of this course is about what it settles at. Every later formula is a function of rho, and the closer rho gets to one, the more violently it moves.

@art queue-forming
And a settled queue isn't an empty one. Even well below one, work waits in line. Why it does, and how much, is where the course goes next.

@chapter Where people slip
@list heading="Common slips" items="Reading μ as a latency@The first|Dividing per-second by milliseconds@The second|Quoting a queue length above ρ = 1@The third"
The first slip is reading mu as a latency: the service takes two milliseconds, so mu is two. It's five hundred. Any rho in the hundreds is this mistake. The second is dividing a per second rate by a millisecond figure. Convert first. And the third is quoting a queue length above rho of one.

@chapter Try it
@words text="λ = 1200/s · S = 1 ms" sub="μ is still 1000/s"
Your turn. Keep the one millisecond service and raise the load to twelve hundred a second. Mu is unchanged at a thousand. Work out rho, say whether it settles, and if it doesn't, give the backlog after five minutes.

@end text="Write the unit next to every number"
You can set the arrival rate and the service time and watch rho cross one, on Learn. That's learn dot get er done dot I O.
