---
format: long
lesson: availability-and-failure/chains-multiply
title: Series availability: why your system is worse than its weakest link
thumb: Worse than the weakest link
---

@chapter The question
@title text="Series: Availability Multiplies" sub="Availability and Failure" art=thumb
They say a system is as available as its weakest link. It isn't. It's worse, by roughly the number of links. Here's the arithmetic.

@art chain-of-boxes
A request that needs every one of its dependencies succeeds only if all of them are up. The auth service, and the database, and the cache, and the network between them. That's an and.

@chapter The product
@math heading="Series availability" items="A = A₁ · A₂ · … · Aₙ = ∏ Aᵢ@the product;;1 − A ≈ Σ (1 − Aᵢ)@add up"
Under independence, the probability of an and is the product. So the chain's availability is the product of the parts. And when each unavailability is small, the outages roughly add up.

@words text="10 links × 1/1000 down ≈ 10/1000 down" sub="about 99%"
That approximation is how you estimate it in a meeting. Ten dependencies, each down one part in a thousand, are down about ten parts in a thousand. So the chain is about ninety nine percent.

@chapter Ten links
@math heading="Ten links at 999/1000" items="A = (999/1000)¹⁰@nine nine nine;;= 99.00449%  ·  two nines@ninety nine point oh oh;;downtime = 7 h 16 min 2.05 s a month@seven hours;;weakest link alone = 43 min 48 s  →  9.96×@forty three minutes"
Exactly, it's nine nine nine over a thousand, to the tenth power. That's ninety nine point oh oh four four nine percent. Two nines, not three. Seven hours sixteen minutes a month, against forty three minutes forty eight for one link. Nine point nine six times the downtime.

@art shrinking-product
Each factor is at most one, so multiplying by it can never raise the total. The chain is below every one of its links. Every link has its own outages, and they accumulate.

@chapter Adding a better service
@math heading="Add one link at 99.99%" items="(999/1000)¹⁰ × (9999/10000)@times;;= 98.99459%  ·  one nine@ninety eight point nine nine"
Now add an eleventh dependency, at ninety nine point nine nine, ten times better than any link already there. The chain becomes ninety eight point nine nine four five nine percent. One nine. The monthly downtime rises to seven hours twenty minutes.

@art extra-link
Multiplying by point nine nine nine nine is still multiplying by something less than one. There's no availability short of exactly one that a chain absorbs for free. Redundancy improves a path. A dependency, however good, only costs it something.

@chapter Reading the number
@math heading="Three nines from ten links" items="A¹⁰ = 0.999  →  A ≈ 0.9998999@each needs;;ten × 99.99%  →  99.90004%@ten four nines"
So you can't build a three nines promise from three nines parts. For ten equal links to reach three nines, each needs about four nines. Ten four nines services in series give ninety nine point nine oh oh oh four percent.

@art shorter-chain
That's why the cheapest way to raise a chain is usually to shorten it. Removing a link helps more than any plausible improvement to one that stays. But count only dependencies a request truly needs. A service called only on a cache miss doesn't belong at full weight.

@chapter A checkout path
@art five-links
Real chains aren't ten identical links. Take a checkout path with five: the edge and the ledger at four nines, auth and payments at three, and the catalogue at ninety nine point nine five. Multiplied, that's ninety nine point seven three oh two five percent.

@list heading="Five unequal links" items="auth 0.0010 · payments 0.0010@auth and payments|catalogue 0.0005@catalogue|edge 0.0001 · ledger 0.0001@the edge|sum 0.0027 · exact 1 − A = 0.0026975@the sum"
That's two nines, and one hour fifty eight minutes a month. Add up the unavailabilities: auth and payments are a thousandth each, catalogue half that, the edge and ledger a tenth of it. The sum is a good estimate, and a better explanation.

@art outage-sum
It says at once that auth and payments are three quarters of the outage, and that improving the edge can't matter. The ratio against the weakest link is two point seven, so the chain behaves like about three equal links.

@chapter Where people slip
@list heading="Common slips" items="As good as the weakest link@The first|Adding a reliable service to improve a path@The second|Multiplying without stating independence@The third"
The first slip is calling a chain as good as its weakest link. The second is adding a very available service and expecting the path to improve. And the third is multiplying without saying that independence was assumed. Services in one rack, or shipped by one pipeline, aren't independent.

@chapter Try it
@words text="add fraud check at 99.995%" sub="unavailability 0.00005 joins the sum"
Your turn. The team wants to add a fraud check at ninety nine point nine nine five percent to the checkout path. Its unavailability joins the sum. Predict the new availability and monthly downtime before computing them. Is it still inside two nines, and what would you remove for three?

@end text="Add a link, watch the product step down"
You can build a chain link by link and watch the running product fall, on Learn. That's learn dot get er done dot I O.
