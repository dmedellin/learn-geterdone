---
format: long
lesson: latency-and-the-tail/packet-loss-and-throughput
title: Packet loss and throughput: why one flow can't fill the link
thumb: 10 Gbit/s link, 1 Mbit/s flow
---

@chapter The question
@title text="Packet Loss and Throughput" sub="Latency and the Tail" art=thumb
A team copies a dataset between two regions over a ten gigabit link, and measures a little over a megabit a second. The link isn't the problem. The disks aren't the problem. Nothing is broken. That combination just has a ceiling.

@art sawtooth
The transfer uses one TCP connection over a hundred millisecond round trip with one percent packet loss. A congestion controlled sender grows its window until a loss, then cuts it. Averaged over that sawtooth, the sustainable rate has a bound.

@math heading="The Mathis bound" items="rate ≤ (MSS / RTT) × 1/√p@the maximum segment size"
For a loss rate p, the rate is at most the maximum segment size over the round trip, times one over the square root of p. Notice what's missing. The link capacity doesn't appear in the expression at all. That's the entire surprise.

@chapter Working it out
@math heading="1460 B · 100 ms · p = 1%" items="MSS / RTT = 1460 / 0.1 = 14 600 B/s@fourteen thousand six hundred;;1/√p = 1/√0.01 = 10@ten;;bound = 146 000 B/s = 1.168 Mbit/s@one point one six eight"
Fourteen sixty byte segments over a tenth of a second is fourteen thousand six hundred bytes a second. One over the square root of nought point nought one is ten. So the bound is a hundred and forty six thousand bytes a second, which is one point one six eight megabits a second.

@art thin-stream
On a ten gigabit link, the flow uses about one ten thousandth of the capacity that was bought. Buying more capacity changes nothing. A ten gigabit link doesn't give you a ten gigabit flow.

@math heading="Streams to fill the link" items="⌈10 000 / 1.168⌉ = 8 562@eight thousand five hundred and sixty two"
How many flows would it take? Ten thousand megabits over one point one six eight, rounded up, is eight thousand five hundred and sixty two parallel streams. That's the honest reason bulk transfer tools open many connections.

@art many-streams
Each flow is still held to its own bound. The link capacity is a bound on all of them together, and the only way to use it is to run enough of them at once.

@chapter The square root
@math heading="Loss against the bound" items="p = 0.1%:  3.694 Mbit/s@nought point one;;p = 1%:  1.168 Mbit/s@one percent;;p = 2%:  0.826 Mbit/s@two percent;;p = 5%:  0.522 Mbit/s@five percent"
Loss enters as one over the square root. At nought point one percent loss, the bound is three point six nine four. At one percent, one point one six eight. At two percent, nought point eight two six. At five percent, nought point five two two.

@art sqrt-curve
So doubling the loss doesn't halve the throughput. It multiplies it by one over the square root of two, about nought point seven zero seven. Anyone who expected nought point five eight four applied the wrong rule. And halving the loss buys forty one percent more, not a hundred.

@chapter Two levers
@math heading="Priced against each other" items="RTT 100 → 10 ms:  11.680 Mbit/s,  × 10@a nearer region;;loss 1% → 0.1%:  3.694 Mbit/s,  × √10 ≈ 3.16@tenfold improvement;;link 10 → 40 Gbit/s:  1.168 Mbit/s,  unchanged@quadruple the link"
Move the round trip from a hundred to ten milliseconds, a nearer region, and the bound becomes eleven point six eight, exactly ten times. A tenfold improvement in loss, a much harder thing to achieve, gives three point six nine four, a factor of about three point one six. Quadruple the link, and nothing changes.

@art two-levers
Distance is the more powerful lever by a factor of three. It's also the one the speed of light said physics cares about.

@chapter Honest limits
@words text="√(1/50) has no rational value" sub="computed by Newton's method"
One honesty note. Every other figure on this course is an exact fraction. This bound contains a square root, and the root needed at two percent loss has no rational value. So the lab computes it by Newton's method, to fifteen decimal places, and says so.

@art ceiling-not-prediction
And it's a bound on the average rate. Retransmission timeouts, a too small receive window and slow start all cost more. It also only describes loss based congestion control. Read it as the ceiling a classical flow can't pass.

@chapter Where people slip
@list heading="Common slips" items="Expecting one flow to reach the link rate@The first|Treating loss as linear@The second|Quoting the bound as exact@The third"
The first slip is expecting one flow to reach the link rate. The second is treating loss as linear, which over promises what a loss reduction will achieve. And the third is quoting the bound as an exact figure. Quote it as a ceiling, to three or four significant figures.

@chapter Try it
@words text="MSS 9000 B · RTT 40 ms · p = 0.5% · 1 Gbit/s link" sub="MSS/RTT = 9000/0.04 = 225 000 B/s"
Your turn. A jumbo frame path: nine thousand byte segments, a forty millisecond round trip, half a percent loss, over a one gigabit link. The first move is nine thousand over nought point nought four, two hundred and twenty five thousand bytes a second. Compute the bound and the streams to fill the link.

@end text="Count the flows, not the link"
You can change the segment size, the round trip and the loss and watch the bound, on Learn. That's learn dot get er done dot I O.
