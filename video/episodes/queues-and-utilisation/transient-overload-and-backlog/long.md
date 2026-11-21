---
format: long
lesson: queues-and-utilisation/transient-overload-and-backlog
title: Transient overload: a one minute spike, a three and a half minute incident
thumb: The backlog is an area
---

@chapter The question
@title text="Transient Overload and Draining the Backlog" sub="Queues and Utilisation" art=thumb
Traffic spikes above capacity for one minute, then goes back to normal. When does latency recover? Not when the spike ends. In this example, the incident lasts three and a half minutes, and the worst moment is the instant the spike stops.

@art spike-profile
Every formula so far assumed a steady state. A spike above mu has none. The system drains at mu. Arrivals run at one rate before the spike, a higher rate for d seconds, then another rate after.

@words text="check first: stable before, headroom after"
Check two things first. The system must have been stable before the spike, or the backlog didn't start at zero. And there must be headroom afterwards, or there's no drain time at all.

@chapter Build the backlog
@math heading="μ = 1000/s · λ_spike = 1500/s for 60 s" items="excess = 1500 − 1000 = 500/s@the excess;;peak = 500 × 60 = 30 000@thirty thousand"
Take mu of a thousand a second, eight hundred before the spike, fifteen hundred during it for sixty seconds, and eight hundred after. The excess is five hundred a second. So the peak backlog, at the end of the spike, is five hundred times sixty, thirty thousand waiting.

@art backlog-area
A backlog is an area, not a rate. It's the excess times how long the spike lasted. Two spikes with the same peak and different durations leave completely different backlogs. A very high spike for two seconds can be a smaller event than a mild one for ten minutes.

@chapter Drain it
@math heading="After the spike, λ = 800/s" items="headroom = 1000 − 800 = 200/s@the headroom;;drain = 30 000 ÷ 200 = 150 s@a hundred and fifty;;worst lag = 30 000 ÷ 1000 = 30 s@thirty seconds;;total = 60 + 150 = 210 s@two hundred and ten"
Once the spike ends, the consumer is still receiving eight hundred a second, so only the headroom, two hundred a second, works through the backlog. The drain takes thirty thousand over two hundred, a hundred and fifty seconds. The worst lag is thirty thousand over a thousand, thirty seconds. And the whole episode is two hundred and ten seconds.

@art asymmetric-triangle
A minute of overload, three and a half minutes of incident. Work arrived five hundred a second faster than it could be handled, and leaves only two hundred a second faster. So every second of spike costs two and a half seconds of recovery.

@words text="recovery = (excess ÷ headroom) × spike length"
That's the general rule. Recovery is the excess over the headroom, times the length of the spike. A system run close to mu has very little headroom, so its recovery multiplier is large. It's the knee again, in another form.

@chapter What the consumer sees
@art lag-peak
The backlog rises to thirty thousand at sixty seconds, then falls to zero at two hundred and ten. It's fifteen thousand at thirty seconds on the way up, and fifteen thousand again at a hundred and thirty five on the way down. Lag peaks the moment the spike ends. An alert on lag fires late in the spike, and clears long after.

@chapter Two edge cases
@art no-drain
Let the rate return to a thousand instead of eight hundred. The headroom is zero, and the thirty thousand is permanent. The lag stays at thirty seconds for ever. Recovery isn't a property of a spike ending. It's a property of the headroom that follows.

@art surge-under-mu
And a surge to nine hundred against a thousand builds no backlog at all, however long it lasts. There's no excess, so no area. It does raise rho from four fifths to nine tenths, which doubles the response time. A real effect, and a different one.

@chapter Where people slip
@list heading="Common slips" items="Expecting recovery when the spike ends@The first|Sizing from the peak, not the area@The second|Steady-state formulas during the surge@The third"
The first slip is expecting latency to recover when the spike ends. The second is sizing from the peak rate instead of the area. And the third is using a steady state formula during the surge. During the spike the honest calculation is the area. The steady state results apply again only once the backlog has drained.

@chapter Try it
@words text="same rates · spike lasts 30 s" sub="excess still 500/s, so the peak halves"
Your turn. Keep everything, but let the spike last thirty seconds instead of sixty. The excess is still five hundred a second, so the peak halves. Predict the drain time, the worst lag and the total episode before you compute them.

@end text="Measure the area, then the headroom"
You can shape the spike and watch the backlog build and drain, on Learn. That's learn dot get er done dot I O.
