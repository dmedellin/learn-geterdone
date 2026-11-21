---
format: long
lesson: scheduling/crashing-a-project-and-the-time-cost-curve
title: Crashing a project: the cheapest day isn't on the obvious activity
thumb: Buy the cheapest day
---

@chapter The question
@title text="Crashing a Project" sub="Scheduling" art=thumb
Your project takes fourteen days and the deadline is nine. You can shorten activities by paying for them. Which days do you buy, in which order, and what's the cheapest bill for each deadline?

@art crash-bar
Each activity has a normal duration and cost, and a crash duration and cost. The difference in days is its crash room. The cost per day bought is its rate: the extra cost, divided by the days saved, assumed constant.

@chapter A linear programme
@math heading="The crashing programme" items="min  Σ rate · y@minimise;;0 ≤ y ≤ normal − crash@crash room;;timing rows, and finish ≤ d@deadline"
Let y be the number of days bought on each activity. Minimise the total of rate times y. Each y is between zero and its crash room. There's a timing row for every precedence, and one row for the deadline. The deadline appears in exactly one row, as its right hand side.

@words text="Normal cost 290, paid whatever the deadline"
The normal costs aren't in the objective, because they're paid whatever happens. On this project that's two hundred and ninety. A constant shifts the curve without bending it.

@chapter Four activities, two paths
@math heading="A, then B and C, then D" items="rates:  A 20,  B 20,  C 15,  D 30@rates;;A B D = 6 + 4 + 3 = 13@thirteen;;A C D = 6 + 5 + 3 = 14@fourteen"
A comes first, then B and C side by side, then D. The rates per day are twenty for A, twenty for B, fifteen for C, and thirty for D. Path A, B, D takes thirteen days. Path A, C, D takes fourteen. So A, C, D is critical, and B has one day of slack.

@art diamond-network
A and D lie on both paths, so a day bought on either shortens the project, whatever else is going on. B and C each lie on one path, so a day there only helps while that path is the long one.

@chapter The first day
@art slack-day
A is the obvious first buy: critical, on both paths, and it always shortens the project. But it costs twenty. The first day costs fifteen, and it's bought on C. Because of the day of slack on B, one day can come off the longer path alone, and C is the cheapest way to do it.

@art both-paths
After that day, both paths are thirteen, and both are critical. Now a day off the finish needs a day off both paths. That's when A, at twenty, on both paths at once, becomes the cheapest thing to buy.

@chapter The exact curve
@math heading="Deadline → crash bill" items="14:  0@fourteen days;;13:  15  ·  C by 1@thirteen;;12:  35  ·  A 1, C 1@twelve;;11:  55  ·  A 2, C 1@eleven;;10:  85  ·  A 2, C 1, D 1@ten;;9:  120  ·  A 2, B 1, C 2, D 1@nine"
At fourteen days, nothing. At thirteen, fifteen, for one day of C. At twelve, thirty five, adding a day of A. At eleven, fifty five, with A's second day. At ten, eighty five, adding D. And at nine, a hundred and twenty, with B and a second day of C as well.

@art convex-curve
Read inwards and the days cost fifteen, then twenty, then thirty, then thirty five. Each day costs at least as much as the one before. Twenty buys A until A runs out of room. Thirty buys D. Thirty five buys two activities at once, B and C, because by then every path must be shortened separately.

@chapter Checking the plan
@art two-checks
The programme can't check itself. So run the critical path passes on the crashed durations. At eleven days the plan gives A four, B four, C four, D three, and the passes finish on day eleven, with all four critical. Then re-solve every piece of the curve from scratch at its endpoint and compare.

@chapter Where people slip
@list heading="Common slips" items="Buying the cheapest activity, not the cheapest day@The first|Counting curve pieces as distinct prices@The second|Trusting the plan without the passes@And the third"
The first slip is buying the cheapest activity rather than the cheapest day. A day bought on an activity with slack shortens nothing. The second is counting curve pieces as distinct prices. A straight chain preset reports three pieces with slopes fifteen, twenty and twenty. And the third is trusting the plan without re running the passes.

@chapter Try it
@words text="Deadline 12: A by 1, C by 1" sub="durations A 5, B 4, C 4, D 3"
Your turn. Take the plan for a deadline of twelve: one day off A and one off C. Write the crashed durations, run the forward pass, and confirm the project finishes on day twelve. Then check the bill is thirty five.

@end text="Slide the deadline yourself"
You can move the deadline and watch which days get bought, and why, on Learn. That's learn dot get er done dot I O.
