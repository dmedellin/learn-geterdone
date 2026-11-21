---
format: long
lesson: queues-and-utilisation/variability-and-kingman
title: Variability and Kingman's approximation
thumb: Halve the variance, halve the wait
---

@chapter The question
@title text="Variability: the Kingman Approximation" sub="Queues and Utilisation" art=thumb
Two services have the same mean service time, the same arrival rate, the same utilisation. One waits twice as long as the other. The difference is variability, and Kingman's approximation puts a number on it.

@art spread-vs-steady
The number that carries variability is the coefficient of variation, c, the standard deviation over the mean. It's dimensionless, and the formula uses its square. Clockwork, where every gap or every service time is the same, has c squared of zero. Memoryless has one. Anything burstier than memoryless has more than one.

@words text="c_a: gaps between arrivals · c_s: service times" sub="never a count of servers"
There are two of them. c a describes the gaps between arrivals, and c s describes the service times. Neither is ever a count of servers. On this course, servers are s.

@chapter The formula
@math heading="Kingman, for ρ < 1" items="W_q ≈ (ρ/(1 − ρ)) × ((c_a² + c_s²)/2) × S@the queueing time"
Kingman says the queueing time is roughly rho over one minus rho, times the average of c a squared and c s squared, times S. Utilisation, times variability, times the work itself.

@art three-factors
It factorises, and that makes it a design tool. Each factor can be attacked on its own: buy headroom, smooth the traffic, or make the work faster.

@chapter Two cases
@math heading="ρ = 4/5,  S = 2 slots" items="c_a² = 1, c_s² = 1:  (4)(1)(2) = 8@both coefficients;;c_a² = 1, c_s² = 0:  (4)(1/2)(2) = 4@service deterministic"
At four fifths and a service time of two slots, with both coefficients equal to one, it's four times one times two, eight. That's exactly the M M one answer, a useful check. Now make the service deterministic, c s squared of zero. It's four times a half times two, four.

@art halved-wait
Making the service time the same every time halves the queueing time, at the same utilisation and the same mean service time. Nothing was bought. An M D one queue waits half of what an M M one queue waits.

@chapter Where it misses
@math heading="The slotted chain, p = 2/5, q = 1/2" items="c_a² = 1 − p = 3/5,  c_s² = 1 − q = 1/2@its own coefficients;;Kingman: (4)((3/5 + 1/2)/2)(2) = 22/5 = 4.4@twenty two fifths;;exact: L_q/p = (8/5)/(2/5) = 4@exact chain says four"
The fairest test is the slotted chain from earlier, fed its own coefficients: three fifths for the arrivals and a half for the service. Kingman says twenty two fifths, four point four slots. The exact chain says four. About ten percent high.

@art formula-vs-exact
That's not a mistake. It's an approximation read outside the regime it was derived for. Kingman's result becomes accurate as rho approaches one, and here it's read at moderate load. The arithmetic is exact. The model is what's approximate.

@words text="use it for factors, not promises"
So use it as a sensitivity tool, where it's excellent. What would halving the variance of this stage be worth? A factor, and factors survive an approximate model far better than absolute numbers. Used as a promise, it's a number with an unstated error bar.

@chapter The levers
@list heading="Pulling the levers" items="Lower c_s²: make the work uniform@make the work uniform|Lower c_a²: smooth the arrivals@smooth the arrivals|Don't raise either by accident@by accident"
To lower c s squared, make the work uniform: fixed batch sizes, a bounded unit of work. To lower c a squared, smooth the arrivals: a token bucket, jittered retries, client side pacing. And don't raise either by accident. Unbounded retries and synchronised timeouts inject variability straight into the arrivals.

@art smoothing
A token bucket in front of a service is a smoother. Bursty arrivals go in, and a steadier stream comes out, so the variability factor falls and the wait falls with it.

@art synchronised-retries
And watch for the opposite. When many clients time out together and retry at the same instant, they arrive as one burst. This formula prices exactly that.

@chapter Where people slip
@list heading="Common slips" items="Only the mean service time matters@The first|An exact calculation is an exact answer@The second|Reading c as a count of servers@The third"
The first slip is believing only the mean service time matters. If you've only measured means, you haven't measured what this formula depends on. The second is treating an exact calculation as an exact answer. And the third is reading c as a count of servers.

@chapter Try it
@words text="ρ = 4/5 · S = 2 · c_a² = 2 · c_s² = 1" sub="variability factor = 3/2"
Your turn. Keep rho at four fifths and S at two, and make the arrivals burstier than memoryless: c a squared of two, c s squared of one. The variability factor becomes three halves. Predict the queueing time, and say what multiple of the M M one answer it is.

@end text="Smooth the work, halve the wait"
You can set both coefficients and compare Kingman with the exact chain, on Learn. That's learn dot get er done dot I O.
