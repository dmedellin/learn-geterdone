---
format: long
lesson: replication-and-consistency/synchronous-writes-wait-for-the-slowest
title: Synchronous replication: waiting for the slowest is not three times slower
thumb: Maxima don't add
---

@chapter The question
@title text="Synchronous Writes Wait for the Slowest" sub="Replication and Consistency" art=thumb
One replica acknowledges a write in sixteen milliseconds at the p ninety nine. So three replicas should take forty eight, right? The real answer is twenty four. Here's why the intuition is exactly twice too high.

@art fan-out
A synchronous write is acknowledged to the client only after every follower has applied it. The leader sends to all of them at once, and waits for the last one to reply.

@chapter The slowest follower
@math heading="Waiting for N − 1 followers" items="P(acked by t) = F(t)^(N − 1)@all of them"
If each follower's reply time is independent with distribution F, the write is acknowledged by time t only if all of them have replied by t. So the probability is F of t, raised to the power N minus one. That's the distribution of the maximum.

@art shared-switch
And independence is a real assumption. Two replicas sharing a rack switch, a hypervisor, or a garbage collector don't reply independently. This arithmetic describes replicas that do.

@chapter One distribution
@list heading="One replica's ack time (ms : weight of 1000)" items="2 : 600@two milliseconds|4 : 300@four|8 : 70@eight|16 : 22 · 24 : 6 · 40 : 2@sixteen"
Here's a measured distribution. Six hundred in a thousand acks take two milliseconds. Three hundred take four. Seventy take eight. Then twenty two take sixteen, six take twenty four, and two take forty.

@math heading="N = 3: the slowest of 2 followers" items="F(16) = 0.992  →  one replica's p99 = 16 ms@one replica;;F(16)² = 0.984064 < 0.99@squared;;F(24)² = 0.998² = 0.996004 ≥ 0.99  →  24 ms@twenty four"
One replica is done by sixteen milliseconds ninety nine point two percent of the time, so its p ninety nine is sixteen. But point nine nine two squared is only point nine eight four. At twenty four, point nine nine eight squared is point nine nine six. So twenty four milliseconds.

@art power-curve
Read that carefully, because it's the whole lesson. Both followers are done by sixteen in ninety eight point four percent of cases. A little worse than one, not twice as bad. That small shortfall against ninety nine is what pushes the p ninety nine out one step.

@chapter Why not three times
@math heading="The claim and the truth" items="claim: 3 × 16 ms = 48 ms@the claim;;truth: 24 ms@the truth;;48/24 = 2.00× too high@twice"
The claim is three times sixteen, forty eight. The truth is twenty four. Exactly twice too high. A power of a number just below one stays close to one, which is nothing like multiplying a time by three.

@art parallel-vs-serial
Latencies of sequential calls add. Latencies of parallel calls don't. They cost the slowest. If your leader forwards to one follower, waits, then forwards to the next, three times is the right arithmetic, and the fix is to fan out.

@art tail-mass
And the mean isn't the story either. The mean ack for one replica is three point five three six milliseconds. The mean wait for the slowest of two is four point seven oh four. The p ninety nine is twenty four, five times the mean. Tail questions are answered by tails.

@chapter The asynchronous price
@math heading="Bytes at risk" items="rate × mean lag × bytes@rate times;;2000/s × 3.536 ms × 400 B ≈ 2828 B ≈ 2.83 kB@two thousand writes"
Drop the wait and replicate in the background. The write's latency is the leader's alone. But data acknowledged to clients that reached no other machine is rate times lag times bytes. At two thousand writes a second, a three point five three six millisecond lag and four hundred bytes a write, that's about two point eight three kilobytes.

@art leader-only
If the leader's disk is lost in that instant, those writes are gone, and their clients were told they succeeded. So the choice is eight milliseconds on the p ninety nine of every write, or two point eight three kilobytes living in one place. Which is worse is a business question. Which is which, this answers.

@chapter Where people slip
@list heading="Common slips" items="Adding replica latencies together@The first|Answering a tail question with a mean@The second|Taking independence for free@The third"
The first slip is adding replica latencies together. The second is answering a tail question with a mean. The third is taking independence for free. Correlated slowness shifts each replica's own distribution, so measure the maximum directly where you can.

@chapter Try it
@words text="N = 5 and N = 9" sub="test 0.998⁴ and 0.998⁸"
Your turn. Same distribution, five replicas and then nine. The exponents are four and eight, so test point nine nine eight to the fourth, and to the eighth. Predict both p ninety nines first, then check, and say why one of them didn't move at all.

@end text="Add followers, watch the tail"
You can set the replica count and read the acknowledged by curve for any distribution, on Learn. That's learn dot get er done dot I O.
