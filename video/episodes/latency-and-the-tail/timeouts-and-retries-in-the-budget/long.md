---
format: long
lesson: latency-and-the-tail/timeouts-and-retries-in-the-budget
title: Timeouts and retries: what they cost and what they kill
thumb: Never time out at the mean
---

@chapter The question
@title text="Timeouts and Retries in the Budget" sub="Latency and the Tail" art=thumb
A call takes eighteen milliseconds on average, so you set the timeout at eighteen. Sounds reasonable. On this service, that throws away fifteen percent of perfectly good calls.

@art timeout-cut
A timeout and a retry count are a pair of numbers, and each has two consequences. The worst case has to fit inside the time the budget gave this call. And the timeout discards every call that would have succeeded after it.

@math heading="Timeout T, retries r" items="worst case = (r + 1) × T@r plus one;;killed = 1 − F(T)@one minus F of T;;all lost = (1 − F(T))ʳ⁺¹@if attempts are independent"
A call with r retries can use r plus one full timeouts before it gives up. That's the worst case. The fraction of good calls killed is one minus F of T, where F is the measured distribution. And the call fails entirely with probability one minus F of T, to the power r plus one, if attempts are independent.

@chapter The service
@list heading="A hundred measured calls" items="45 at 8 ms · 25 at 11 ms · 15 at 16 ms@forty five calls at eight|8 at 24 ms · 4 at 45 ms@eight at twenty four|2 at 90 ms · 1 at 400 ms@two at ninety"
Here's the lab's service. Forty five calls at eight milliseconds, twenty five at eleven, fifteen at sixteen. Eight at twenty four, four at forty five. Two at ninety, and one at four hundred.

@art budget-box
Its median is eleven, its p ninety five is forty five, its p ninety nine is ninety, and its mean is eighteen point two seven. The budget gives this call two hundred and fifty milliseconds, and every attempt has to fit inside that box.

@chapter Reading the table
@math heading="Budget: 250 ms" items="T = 18:  worst 36 ms,  kills 15.00%@eighteen;;T = 45:  worst 90 ms,  kills 3.00%@forty five;;T = 90:  worst 180 ms,  kills 1.00%@ninety;;T = 90, r = 2:  270 ms > 250 ms  ✗@two retries"
With one retry: a timeout of eighteen has a worst case of thirty six and kills fifteen percent. At forty five, ninety, and three percent. At ninety, a hundred and eighty, and one percent. But ninety with two retries needs two hundred and seventy, and that doesn't fit.

@art retry-pair
So choose a timeout of ninety with one retry. A single attempt is abandoned one time in a hundred. With one independent retry, both are abandoned one time in ten thousand. You've bought two decimal places of reliability for a doubling of the worst case.

@art gap-in-distribution
And a timeout of a hundred and twenty five, with one retry, uses the whole two hundred and fifty and kills the same one percent. There's nothing in the distribution between ninety and four hundred for the extra patience to rescue. Place timeouts against the gaps in the distribution.

@chapter The mean is the worst place
@art mean-timeout
The mean sits in the sparse region above the bulk and below the tail. A timeout there is close enough to the bulk to catch ordinary variation, and far enough from the tail to be no protection against calls that are really stuck. Fifteen in every hundred good answers become errors and retries.

@chapter Retries and overload
@art overloaded-retry
The independence assumption needs scepticism. If the call timed out because the far side is overloaded, the retry is a second request to an overloaded service. Its chance of timing out isn't one in a hundred. It's close to one. Retries against a saturated dependency are a load multiplier, which is why the retry count is capped.

@words text="quote (r + 1) × T  and  1 − F(T)"
So whenever a timeout is proposed, quote two figures together: the worst case against the allocation, and the kill fraction against the measured distribution. On this sample, the mean and the p ninety nine differ by a factor of fifteen in what they throw away.

@chapter Where people slip
@list heading="Common slips" items="Timing out near the mean@The first|Budgeting the typical case@The second|Assuming retries are independent@The third"
The first slip is setting the timeout at or near the mean. The second is budgeting the typical case instead of r plus one times T. The worst case is what happens when the dependency is in trouble, the only time any of this matters. And the third is assuming retries are independent of the failure that caused them.

@chapter Try it
@words text="allocation 150 ms" sub="at T = 90: ⌊150/90⌋ = 1 attempt, no retry"
Your turn. Same sample, but the allocation is a hundred and fifty. At a ninety millisecond timeout, only one attempt fits, so there's no retry. Work out whether forty five with one retry fits, what it kills, and its failure probability. Then choose.

@end text="Quote the worst case and the kill fraction"
You can set the timeout and the retries and see both figures against the budget, on Learn. That's learn dot get er done dot I O.
