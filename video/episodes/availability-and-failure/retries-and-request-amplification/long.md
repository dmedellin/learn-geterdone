---
format: long
lesson: availability-and-failure/retries-and-request-amplification
title: Retries and request amplification: cheapest when you don't need them
thumb: Retries cost most on the bad day
---

@chapter The question
@title text="Retries and Request Amplification" sub="Availability and Failure" art=thumb
Retrying a failed request seems like free reliability. Usually it is cheap. But the same policy that costs eleven percent on a good day can triple your load on a bad one. Here's the arithmetic.

@art retry-ladder
A policy of r retries makes up to r plus one attempts, and stops at the first success. The first attempt always happens. The second only if the first failed. The third only if both failed.

@chapter Two geometric series
@math heading="Each attempt fails with probability p" items="attempts = 1 + p + p² + … + pʳ@the expected number;;= (1 − pʳ⁺¹)/(1 − p)@one minus p;;success = 1 − pʳ⁺¹@succeeds"
So the expected number of attempts is one plus p plus p squared, up to p to the r. That's one minus p to the r plus one, over one minus p. And the request succeeds unless all attempts fail, so with probability one minus p to the r plus one.

@math heading="p = 1/10, r = 2, 500 rps" items="first: 500/s · retry 1: 50/s · retry 2: 5/s@five hundred;;attempts = 111/100 = 1.11  →  555/s@one point one one;;success = 999/1000 = 99.9%@nine nine nine"
At a ten percent failure rate, two retries, and five hundred requests a second, the first attempts are five hundred a second, first retries fifty, second retries five. That's one point one one attempts per request. And success is nine nine nine in a thousand.

@words text="11% more load · 100× less loss"
Eleven percent more load, for a hundredfold reduction in loss. That's an easy trade, and it's the trade every default retry setting is quietly making. The trouble is that eleven percent isn't a constant.

@chapter The bad day
@math heading="r = 2 at four failure rates" items="p = 0.10:  1.110 attempts · 99.9000%@point one;;p = 0.50:  1.750 · 87.5000%@a half;;p = 0.90:  2.710 · 27.1000%@point nine;;p = 0.99:  2.970 · 2.9701%@point nine nine"
Watch the same two retry policy as p rises. At point one, one point one one attempts and ninety nine point nine percent success. At a half, one point seven five and eighty seven and a half. At point nine, two point seven one attempts, twenty seven percent success. At point nine nine, nearly triple the load, for three percent.

@art cost-and-benefit
As p approaches one, the attempts approach r plus one, and success goes to zero. The policy is at its most expensive and least useful in the same regime. Cheapest when it's least needed.

@chapter Failures that can't succeed
@art same-wall
And the independence assumption is generous. A malformed payload fails every time. So does a bad credential, or a missing key. Retrying those pays the full amplification for nothing, and returns the same error more slowly. Classify errors before configuring retries.

@art duplicate-work
The same series counts duplicate work. If an attempt can succeed at the server but its response times out, every extra attempt is a duplicate. At point one and two retries, that's nine point nine one percent of the server's work. It's why at least once delivery needs idempotent handlers.

@chapter Retries multiply along a chain
@math heading="Three tiers, each r = 2, p = 0.1" items="1.11 · 1.11² · 1.11³ ≈ 1.368@one point one one"
Three tiers, each retrying twice. The first tier sees one point one one, the second one point one one squared, the third about one point three seven. A thirty seven percent surcharge on the innermost service, from a policy that looked like eleven at each hop.

@art tier-stack
And when the innermost service degrades, every tier above it starts retrying at once. The innermost sees the product of three bad day factors.

@art retry-budget
The standard fix is a retry budget: a cap, typically a few percent, on the share of a client's traffic that may be retries, enforced across the whole client. At point nine nine, retries would be sixty six percent of the load. The cap doesn't make retries cheaper. It bounds them by something other than r plus one.

@chapter Where people slip
@list heading="Common slips" items="Treating retries as free@The first|Retrying failures that can't succeed@The second|Counting amplification once on a multi-tier path@The third"
The first slip is treating retries as free because they usually succeed. Capacity has to cover lambda times r plus one. The second is retrying failures that can't succeed. The third is counting the amplification once on a multi tier path, when it multiplies.

@chapter Try it
@words text="capacity 5000 rps · offered 2000 rps" sub="binding constraint: λ × (r + 1)"
Your turn. A service handles five thousand a second, with two thousand offered. The binding constraint is the ceiling, lambda times r plus one. Find the largest r whose worst case fits, then its success probability at a half and at point nine.

@end text="Raise p, watch the load climb"
You can set the retries and the failure rate and watch the cost rise as the benefit falls, on Learn. That's learn dot get er done dot I O.
