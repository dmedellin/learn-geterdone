---
format: long
lesson: inventory-models/periodic-review-and-the-base-stock-level
title: Periodic review: why base stock must cover R plus L
thumb: Cover R + L, not L
---

@chapter Looking every R periods
@title text="Periodic Review and the Base-Stock Level" sub="Inventory Models" art=thumb
Not every shelf is watched all the time. Often someone checks it once a week and tops it up. That one change makes the stock you need much bigger than it looks.

@art order-up-to
Here's the policy. Every R periods, the review interval, you inspect the stock and order enough to bring what's on hand plus on order up to a base stock level, S. The order arrives after a lead time of L periods.

@words text="S is a position, not an order quantity"
So S is a target position. The order you place is S minus what's already on hand and on order, so the amount changes from review to review, while S stays put.

@chapter The exposure window
@art review-timeline
Now, how long does today's stock position have to last? The order placed now arrives at L. But if demand runs high, your next chance to act is the next review, at R, and that order lands at R plus L.

@words text="Window = R + L"
So the position you take now is the last one that can affect stock until R plus L. It has to cover demand over that whole span. Think about when your next chance to act arrives, not when this order does.

@math heading="The two limits" items="L = 0:  window R@lead time of zero;;R = 1:  window 1 + L@every period"
Check the limits. With a lead time of zero, the window is still R, because you can't order again until the next review. And reviewing every period gives one plus L, the continuous review answer with one period of granularity.

@chapter The worked instance
@art three-period-hump
Demand is zero, one or two a period, with probabilities a quarter, a half, a quarter. Review every two periods, lead time one. So the window is three periods: convolve three times. Mean three, from zero to six, piled in the middle.

@math heading="Cumulative over 3 periods" items="S = 2:  11/32 = 34.38%@two;;S = 3:  21/32 = 65.63%@three;;S = 4:  57/64 = 89.06%@four;;S = 5:  63/64 = 98.44%@five"
The cumulative chance of covering demand: at S of two, thirty four point three eight percent. At three, sixty five point six three. At four, eighty nine point oh six, just short of ninety. At five, ninety eight point four four percent.

@art overshoot-step
So for a ninety percent target, S is five, and it actually achieves ninety eight point four four. Nothing lies between, so you overshoot by more than eight points and hold a unit you didn't ask for. Report the achieved level beside the target.

@chapter Covering the lead time alone
@art lead-only-window
Here's the standard mistake. Cover only the lead time: one period, quantiled at ninety percent, gives S of two. Sensible looking. But over the real three period window, a level of two delivers only eleven thirty seconds, thirty four point three eight percent, against a target of ninety.

@words text="Target 90% · delivered 34.38%"
That isn't slightly under stocked. It's wrong by a factor, and every figure used to produce it was computed correctly. Nothing in the arithmetic will reveal it.

@chapter Longer lead, and the trade
@words text="L = 2 → window 4 · S = 6 at 96.48%"
Raise the lead time to two periods, so the window is four. The mean is four, and S for ninety percent rises to six, achieving ninety six point four eight percent. Both letters, R and L, do work.

@art continuous-vs-periodic
Continuous review is exposed only for L. Periodic review is exposed for R plus L. That extra stock is the price of not watching. Review more often and you spend effort but hold less. Review less often, and it's the other way round.

@chapter Where people slip
@list heading="Common slips" items="Covering L and forgetting R@The first|Ordering S units every review@The second|Reporting the target, not the achievement@And the third"
The first slip is covering the lead time and forgetting the interval. The second is ordering S units at every review, which ignores what's already coming and makes the system oscillate. And the third is reporting the target instead of what you achieve.

@chapter Try it
@words text="Targets 95% and 99%" sub="R = 2 · L = 1"
Your turn. Using the same cumulative table, find S for a ninety five percent target and for ninety nine percent, and the service each actually achieves. You should get five, then six at a hundred percent.

@end text="Cover the whole window"
You can change the review interval and lead time and watch the right and wrong levels side by side, on Learn. That's learn dot get er done dot I O.
