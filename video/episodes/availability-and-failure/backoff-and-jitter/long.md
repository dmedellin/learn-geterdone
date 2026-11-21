---
format: long
lesson: availability-and-failure/backoff-and-jitter
title: Backoff and jitter: why exponential backoff alone doesn't save you
thumb: Spread the herd
---

@chapter The question
@title text="Backoff and Jitter" sub="Availability and Failure" art=thumb
Exponential backoff is the standard advice for retries. It does fix the total number of retries. But it does nothing at all to the peak. And the peak is what decides whether a service survives coming back.

@art synced-waves
An outage is a moment when every client fails at once. Each schedules its first retry one base delay later. Since the failures were simultaneous, so are the retries.

@chapter Backoff makes waves
@math heading="Exponential backoff" items="delay before attempt i = base × 2ⁱ⁻¹@base times two;;waves at 1, 2, 4, 8, 16, 32 s@one, two, four"
Under exponential backoff, the delay before attempt i is the base times two to the i minus one. With a one second base, the waves land at one, two, four, eight, sixteen and thirty two seconds. Doubling a constant leaves it constant.

@art doubling-gaps
Backoff is a real improvement in one way. A client makes six attempts in forty seconds rather than forty. But all six land in six instants, and at each instant the rate is the whole client population.

@words text="600 clients · 6 waves · 3600 retries" sub="peak 3000/s in 200 ms slots"
Take six hundred clients and a twenty second outage. Six waves of six hundred is three thousand six hundred retries. Measured in two hundred millisecond slots, the peak is three thousand a second.

@art narrow-spike
And that's a floor, not a measurement. Without jitter, every client in a wave retries in the same millisecond. Any bucket wider than that understates the spike. Report the resolution with the number.

@chapter Jitter spreads them
@math heading="Jitter of width w" items="delay ~ Uniform[d(1 − w/2), d(1 + w/2))@draws the delay uniformly;;w = 100%  →  [0.5d, 1.5d)@full width"
Jitter draws the delay uniformly from an interval centred on the nominal delay d. With full width jitter, attempt i is spread over half d to one and a half d.

@math heading="Same 600 clients, seed 7" items="peak:  3000/s  →  925/s@the peak;;factor 3.24@a factor;;total:  3600  →  3323@the total"
Run the same clients with full width jitter. The peak falls from three thousand a second to nine hundred and twenty five. That's a factor of three point two four, from the same policy and the same seed. The total falls slightly, from three thousand six hundred to three thousand three hundred and twenty three.

@art smeared-waves
That small drop in total is a side effect. A jittered retry that lands after the service has recovered succeeds, and the client stops. Jitter isn't a way to reduce total load. It's a way to spread it.

@chapter What the service sees
@art recovery-capacity
A service coming back after twenty seconds gets a first second of either three thousand requests or about nine hundred, depending on one setting. If it can handle fifteen hundred a second, the first case fails again. And every client that fails re-enters the schedule, the retry storm with a synchronised phase.

@words text="Same mean delay" sub="half the draws earlier, half later"
And jitter doesn't increase the mean delay, because the interval is centred on d. What it costs is predictability for one client, and that's almost never a cost anyone is paying. Half width jitter leaves the waves partly visible, and peaks at twelve hundred and forty.

@chapter A thundering herd
@math heading="2000 clients · recovery capacity 1200/s" items="no jitter:  peak 10 000/s@Without jitter;;100% jitter:  peak 3075/s · total 11 597@with full width;;3075/s vs 1200/s@still nearly three times"
Now two thousand clients, and a service that can handle twelve hundred a second while recovering. Without jitter, the peak is ten thousand a second. With full width jitter, three thousand and seventy five. That's still nearly three times what it can serve.

@art not-sufficient
So jitter is necessary, and not sufficient. The rest of the gap closes somewhere else: a larger base delay, a retry budget, or refusing the excess at the door. And size against recovery capacity. Cold caches and empty pools make it lower than steady state.

@chapter Where people slip
@list heading="Common slips" items="Using backoff without jitter@The first|Measuring the peak in wide buckets@The second|Judging jitter by the total@The third"
The first slip is using backoff without jitter. The second is measuring the peak in buckets wider than the wave. A one second bucket divides it by a thousand. The third is judging jitter by the total instead of the peak.

@chapter Try it
@words text="2000 clients · 1200/s" sub="peak ≈ clients/base, a lower bound"
Your turn. Keep two thousand clients and twelve hundred a second. Find the backoff base at which the jittered peak first fits. Full width jitter spreads wave one over about the base, so the peak is roughly clients over base. Estimate, then check, and say how far out you were.

@end text="Turn jitter on, watch the waves smear"
You can replay the same seeded outage with and without jitter and read the peak, on Learn. That's learn dot get er done dot I O.
