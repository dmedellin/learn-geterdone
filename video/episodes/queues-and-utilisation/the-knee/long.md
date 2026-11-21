---
format: long
lesson: queues-and-utilisation/the-knee
title: The knee: response time against utilisation
thumb: The last few percent
---

@chapter The question
@title text="The Knee: Response Time vs Utilisation" sub="Queues and Utilisation" art=thumb
Going from fifty percent busy to ninety percent makes requests wait five times as long. Going from ninety to ninety nine makes them wait ten times longer again. Nine points cost more than forty. Here's the curve that explains it.

@math heading="From the M/M/1 queue" items="W = 1/(μ − λ)@one over mu minus lambda;;= S/(1 − ρ)@S over one minus rho;;W/S = 1/(1 − ρ)@Divide through by S"
From the M M one queue, the time in system is one over mu minus lambda. Divide top and bottom by mu, and that's S over one minus rho, where S is the service time. Divide through by S, and the response time factor is one over one minus rho.

@art hyperbola
That's how many service times a request spends in the system. It's one at rho of zero, the work and nothing else, and it's unbounded as rho approaches one. It's a hyperbola, with its asymptote at rho of one.

@chapter Three points
@math heading="S = 10 ms" items="ρ = 1/2:  W/S = 2,  W = 20 ms@a half;;ρ = 9/10:  W/S = 10,  W = 100 ms@nine tenths;;ρ = 99/100:  W/S = 100,  W = 1000 ms@ninety nine hundredths"
Take a ten millisecond service. At a half, the factor is two, so twenty milliseconds. At nine tenths, ten, so a hundred. At ninety nine hundredths, a hundred, so a full second.

@art queue-at-high-load
Same work, same server. The only thing that changed is how busy it is. At ninety nine percent, a request spends a full second in the system, and only ten milliseconds of that is the work itself.

@art headroom-axis
The utilisation axis is the wrong one to reason on. The headroom axis, one minus rho, going a half, a tenth, a hundredth, is what the response time is really a function of. Halve the spare capacity, and the response time doubles, wherever you started.

@words text="the knee is not a point"
The knee isn't a particular point on this curve. It's the fact that the curve has no particular point, and that the interesting region is always the last few percent.

@chapter Reading it backwards
@math heading="Tolerate W = kS" items="1/(1 − ρ) = k@one over;;ρ = (k − 1)/k@k minus one over k;;headroom = 1/k@one over k"
Nobody picks a utilisation and accepts the response time that falls out. Name what you'll tolerate instead, W equals k times S, and solve. One over one minus rho equals k gives rho as k minus one over k. The headroom you must keep is exactly one over k.

@list heading="Targets" items="k = 2 → ρ = 1/2@twice|k = 4 → ρ = 3/4@four times|k = 10 → ρ = 9/10@ten times|k = 100 → ρ = 99/100@a hundred times"
Tolerating twice the service time means running at a half. Four times means three quarters. Ten times means nine tenths. A hundred times means ninety nine hundredths, where a single machine failure in a pool is an outage rather than an event.

@art capacity-target
This is where a capacity plan's target utilisation comes from. A plan that names eighty percent has chosen k of five, whether or not anybody said so.

@chapter The same doubling
@art doubling-two-ways
A service at a half absorbs a doubling of traffic and moves from two service times to four, which nobody notices. The same doubling at nine tenths isn't survivable at all. Rho would be nine fifths, above one, and there's no response time to quote, only a growth rate.

@chapter Caveats
@art tail-beyond-mean
The one over one minus rho shape is general, but the constant in front is the M M one constant. It depends on how variable arrivals and service are. And W is a mean. Percentiles sit further out still. No faster disk or tuning moves the asymptote either. Those change S, which scales the curve.

@chapter Where people slip
@list heading="Common slips" items="Expecting W to grow with load@The first|Planning to a maximum utilisation@The second|Quoting S/(1 − ρ) as universal@The third"
The first slip is expecting response time to grow with load. It grows with the reciprocal of the headroom, so linear extrapolation underestimates by an order of magnitude. The second is planning to a maximum utilisation. The box can do ten thousand a second is a statement about rho of one. And the third is quoting the formula as universal.

@chapter Try it
@words text="S = 4 ms · tolerate W = 5S" sub="k = 5 gives ρ = 4/5"
Your turn. A four millisecond service, and you'll tolerate five service times. That gives rho of four fifths. Compute W at that target. Then compute W if the service time degrades to five milliseconds, with the load unchanged.

@end text="Plan to a headroom, not a maximum"
You can drag the utilisation along the curve and read W off it, on Learn. That's learn dot get er done dot I O.
