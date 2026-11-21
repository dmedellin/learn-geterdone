---
format: long
lesson: simulation-and-variance-reduction/common-random-numbers
title: Common random numbers: compare two systems with the same stream
thumb: Same draws, sharper difference
---

@chapter Comparing two systems
@title text="Common Random Numbers" sub="Simulation and Variance Reduction" art=thumb
Is a faster server worth it? You simulate both systems and compare. But the question is about their difference, and the difference has a variance of its own, with a term you can control for free.

@math heading="The variance of a difference" items="Var(A − B) = Var A + Var B − 2·Cov(A, B)@the variance"
Here's the identity. The variance of A minus B is the variance of A, plus the variance of B, minus twice their covariance. Expand the square and take expectations. Nothing about the two distributions was used, so it always holds.

@words text="Make Cov(A, B) positive"
So anything that makes the covariance positive takes twice it off the variance of the difference. That's the entire mechanism. If the covariance doesn't go positive, the technique hasn't worked.

@chapter Share the stream
@art shared-stream
Common random numbers means driving both systems from the same stream of draws, so replication j of system A and replication j of system B see the same randomness.

@art separate-streams
The alternative is the independent scheme: a fresh stream for each system. That's the one we'll compare against.

@art move-together
In the lesson's queue, the two systems differ only in the service rate. The arrival test in slot t reads draw t, so both systems see exactly the same arrivals. A busy stretch is busy for both. Their outputs rise and fall together, and the covariance goes positive.

@words text="Arrival draw t · service draw i" sub="fixed indices, not event order"
One implementation detail matters. Each slot's arrival reads a fixed draw, and each customer's service reads another fixed draw. Consume one stream in event order instead, and the two runs quietly drift apart, and you'd measure less correlation than the method actually gives.

@chapter The measurement
@words text="A: q = 1/2 · B: q = 3/5 · p = 2/5" sub="means 12/5 and 6/5 · difference 6/5"
System A has a service probability of a half, system B three fifths, both with arrivals at two fifths. Exact means twelve fifths and six fifths, so the true difference is six fifths. Twenty four replications of two hundred slots.

@math heading="Shared stream" items="Var A 1.53075 · Var B 0.19979@shared stream;;Cov(A, B) = 0.46132@covariance;;1.53075 + 0.19979 − 2(0.46132) = 0.80790@check"
With a shared stream, the variance of A is about one point five three, and of B about point two. The covariance is about point four six. Check the identity: one point five three plus point two, minus twice point four six, gives about point eight oh eight.

@art move-apart
With separate streams, the covariance is about minus point one eight. Not zero, just an estimate of zero, landing slightly negative. The variance of the difference is about two point one oh.

@art difference-spread
So point eight oh eight against two point one oh, a factor of two point six oh four. The two estimates, one point one three and one point oh nine, are both aiming at one point two, and neither is better. The only thing bought is the precision of the difference.

@chapter The factor is an estimate
@words text="Seed 1: 2.604 · seed 0: 5.770 · seed 7: 1.823"
Change the seed, and the factor moves: five point seven seven at seed zero, and one point eight two at seed seven. The covariance is reliably positive, but its size is a measurement with its own spread. Don't quote it to three figures from one seed.

@art nested-arrivals
The second pair changes the arrival probability too, two fifths against a half. Every arrival in the first is an arrival in the second, so the arrival streams are nested, and the factor here is about five. How much you gain depends on how the runs happen to couple.

@chapter Where people slip
@list heading="Common slips" items="Crediting the pairing on one system@The first|Thinking independent runs are fairer@The second|Not computing both variances@And the third"
The first slip is claiming a narrower error bar on one system. A's own variance is one point five three in both schemes. The second is thinking independent runs are fairer. Both are unbiased; independent ones are just noisier. And the third is declaring success without computing both variances and dividing.

@chapter Try it
@words text="Var A + Var B (separate)" sub="1.53075 + 0.21668"
Your turn. Add the separate stream variances of A and B, and compare with the separate variance of the difference, two point one oh three six seven. Use the identity to explain the gap of about point three five six.

@end text="Share the stream, measure the gain"
You can switch between shared and separate streams and watch the covariance, on Learn. That's learn dot get er done dot I O.
