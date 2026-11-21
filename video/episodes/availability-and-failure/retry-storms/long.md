---
format: long
lesson: availability-and-failure/retry-storms
title: Retry storms: how 95 percent load settles at 173 percent
thumb: The retries are the overload
---

@chapter The question
@title text="Retry Storms" sub="Availability and Failure" art=thumb
Your service runs at ninety five percent of capacity. That's tight, but it's inside. Add three retries, and it settles at a hundred and seventy three percent, and stays there. Here's the loop that does it.

@art feedback-loop
Load raises the failure rate. The failure rate raises the amplification. And the amplification raises the load. Each one feeds the next, around and around.

@chapter The map
@math heading="The retry-storm map" items="p(L) = base + (1 − base)·max(0, (L − C)/L)@the failure rate;;L′ = λ · (1 − p(L)ʳ⁺¹)/(1 − p(L))@the new load"
Here's the model. Below capacity, the failure rate is just its base value. Above it, the server finishes only C over L of the work, so the failure rate rises by the overload share. And the new load is the offered load times the attempts that failure rate produces.

@words text="Capacity is the unit: C = 1" sub="λ = 0.95, base = 10%, r = 3"
Every load is a multiple of capacity, so capacity is one. Offered load is point nine five. The base failure rate is ten percent, and there are three retries.

@chapter Iterating by hand
@math heading="Five steps" items="0.95  →  1.05545@The first step;;1.05545  →  1.11356@Then one point one one;;1.11356  →  1.17384@one point one seven;;1.17384  →  1.23538@one point two three;;1.23538  →  1.29693@one point two nine"
The first step alone crosses capacity. Point nine five times one point one one one is one point oh five five. Then one point one one, one point one seven, one point two three, one point two nine. It keeps climbing.

@art staircase-up
Every figure in each row came from the row above it. Nothing outside the system changed between the steps. The loop is doing all of it.

@math heading="Step two" items="(1.05545 − 1)/1.05545 = 0.05254@the overload share;;p = 0.1 + 0.9 × 0.05254 = 0.14728@the failure rate is;;attempts = 1.17217  →  0.95 × 1.17217 = 1.11356@four attempts"
Work step two by hand. The overload share is point oh five two five. So the failure rate is point one plus point nine times that, point one four seven three. Four attempts at that rate cost one point one seven two, and point nine five times that is one point one one three six.

@art growing-digits
But exact iteration can't get there. Each step cubes the denominator. Five digits, then thirteen, thirty nine, a hundred and nineteen, three hundred and fifty eight. By the seventh step, over three thousand.

@chapter Bracketing the fixed point
@art bisection
So bracket it instead. The map rises with load and is capped at lambda times r plus one. So the gap between the new load and the old changes sign in that range, and bisection traps the root without anything compounding.

@math heading="The fixed point" items="L* = 1.72736@one point seven two seven;;p = 0.47897 · amplification 1.8183@the failure rate there;;0.95 × 1.8183 = 1.72739 ≈ L* ✓@check"
The fixed point is one point seven two seven times capacity. The failure rate there is forty seven point nine percent, and the amplification is one point eight one eight. Check: point nine five times one point eight one eight three is one point seven two seven.

@art switch-off
And that failure rate is what sustains the amplification that made the load. Turn the retries off and the load drops straight back to point nine five. The overload has no outside cause. That's why it doesn't end when the original trigger does.

@chapter A cliff, not a slope
@list heading="Offered load → fixed point" items="0.80  →  0.8888@point eight|0.90  →  0.9999@point nine settles|0.95  →  1.727@point nine five"
The transition isn't gradual. Point eight settles at point eight eight eight eight. Point nine settles at point nine nine nine nine, both inside capacity. Point nine five settles at one point seven two seven. Fine, fine, then eighty percent over.

@art cliff
Below the cliff, the load never crosses capacity, so the failure rate never leaves its base value, and the loop is switched off. That's why a retry policy looks harmless right up until it isn't.

@list heading="λ = 0.95, vary r" items="r = 0:  0.95@no retries|r = 1:  1.168@one retry|r = 2:  1.439@Two, one point|r = 3:  1.727@Three, one point"
Now hold the load at point nine five and vary only the policy. No retries gives point nine five. One retry, one point one six eight. Two, one point four three nine. Three, one point seven two seven. Same traffic, same service. The policy is the whole overload.

@chapter Where people slip
@list heading="Common slips" items="Believing retries stop when the service recovers@The first|Sizing capacity against the offered load@The second|Iterating the exact map to the answer@The third"
The first slip is believing the retries stop when the service recovers. They're what stops it recovering. The second is sizing capacity against the offered load instead of the fixed point. The third is iterating the exact map to the answer. Bracket it.

@chapter Try it
@words text="base = 0.05 · r = 2" sub="below C, amplification is 1.0525"
Your turn. Base failure five percent, two retries. While load stays under capacity, amplification is a constant one point oh five two five. So the loop engages once lambda times that exceeds one. Solve for the offered load where the storm starts.

@end text="Slide the load across the cliff"
You can step the offered load and the retry count and watch the fixed point jump, on Learn. That's learn dot get er done dot I O.
