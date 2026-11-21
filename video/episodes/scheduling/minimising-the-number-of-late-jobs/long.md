---
format: long
lesson: scheduling/minimising-the-number-of-late-jobs
title: Fewest late jobs: throw out the longest, not the one that's late
thumb: Throw out the longest
---

@chapter The question
@title text="Minimising the Number of Late Jobs" sub="Scheduling" art=thumb
Sometimes lateness is all or nothing. A shipment made the sailing or it didn't. Then you want as few late jobs as possible, and how late they are doesn't count. That changes the problem completely, because a job can be written off and pushed to the end at no extra cost.

@chapter Moore and Hodgson's algorithm
@art offer-queue
This objective has an exact algorithm, not a sorting rule. Offer the jobs one at a time in due date order. Keep a set of accepted jobs and a running finish time. Add each job, and advance the clock by its processing time.

@art discard-longest
If the finish time now passes the due date of the job just added, throw out the longest job in the set, and take its time back off the clock. Not the job that just went late. The longest one. At the end, the set is the largest group that can all be on time.

@chapter Five jobs, five steps
@math heading="Offered in due-date order" items="B joins:  finish 4,  due 4,  on time@B joins;;D joins:  finish 7,  due 6,  late  →  discard B@D joins;;A joins:  finish 9,  due 8,  late  →  discard A@A joins;;C joins:  finish 8,  due 12,  on time@C joins;;E joins:  finish 15,  due 20,  on time@E joins"
B joins, finishing at four, due at four, on time. D joins, finishing at seven, due at six, late. Throw out the longest, B, and the clock drops to three. A joins, finishing at nine, due at eight, late. The longest is A itself, so A goes. C joins, finishing at eight, on time. E joins, finishing at fifteen, on time.

@art set-overflow
Look again at step two. D is the job that pushed the set past a due date, so the instinct is to throw D out. Either choice leaves one job late, so they tie on the objective. But D frees three hours and B frees four. That extra hour is what lets C and E both join later.

@words text="B was never the problem"
B had been comfortably on time at step one, and it's thrown out at step two without ever having been the problem. That's the move that feels wrong and is right.

@chapter The result
@math heading="Kept D C E, discarded B and A" items="schedule  D C E B A@schedule;;finish 3, 8, 15, 19, 25@finishing;;late: 2@two late"
So the algorithm keeps D, C and E, and discards B and A. Run the kept set in due date order, then the discarded ones. The schedule is D, C, E, B, A, finishing at three, eight, fifteen, nineteen and twenty five. Two late. And checking all hundred and twenty orders, two late is the minimum.

@art kept-on-time
The kept set really is on time, checked job by job: D at three against six, C at eight against twelve, E at fifteen against twenty. If a set can be on time at all, it can be on time in due date order.

@chapter The rules it beats
@list heading="Late jobs" items="Due-date order alone: 4@Due date order alone|Shortest first: 3@Shortest first|Moore–Hodgson: 2@the algorithm"
Due date order alone leaves four late. It keeps trying to run B and A on time, fails at both, and the hours spent failing make C late too. Shortest first leaves three. And the algorithm leaves two. Writing two jobs off at the start is what buys the other three.

@chapter What it ignores
@art late-at-end
It doesn't minimise total tardiness, and doesn't try. B finishes at nineteen against a due date of four, and A at twenty five against eight. That's thirty two hours of tardiness, against seventeen for due date order. The objective counts jobs, so it doesn't care.

@art weighted-discards
And it doesn't handle weights. The argument rests on every discard costing exactly one. If a missed date on one job costs ten times another, that's a genuinely harder problem, and this algorithm would answer the wrong question confidently.

@chapter Where people slip
@list heading="Common slips" items="Discarding the job that went late@The first|Reading the offer order as the answer@The second|Using it when late jobs aren't equal@And the third"
The first slip is discarding the job that went late. The second is reading the offer order as the answer. The schedule is D, C, E, B, A, not due date order. And the third is using it when the late jobs aren't all worth the same.

@chapter Try it
@words text="At step 2, discard D instead" sub="then keep offering A, C, E"
Your turn. Rerun the five steps, but at step two throw out D, the job that went late, instead of B. Carry on offering A, C and E with the same rule after that. Count how many jobs end up late, and compare with two.

@end text="Offer, accept and discard"
You can step through the offers and watch which job gets thrown out, on Learn. That's learn dot get er done dot I O.
