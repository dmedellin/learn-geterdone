---
format: long
lesson: queues-and-utilisation/littles-law-from-a-trace
title: Little's Law from a trace: one area, counted two ways
thumb: L = λW, by counting
---

@chapter The question
@title text="Little's Law from a Trace" sub="Queues and Utilisation" art=thumb
L equals lambda W is quoted next to queueing models so often that people think it needs one. It doesn't. It isn't a model or an approximation. It's one area, counted two ways. Let's prove it on five customers.

@art staircase
Over a window from zero to T, n customers arrive and leave. N of t is how many are inside at time t. L is the time average of N of t, the area under it over T. Lambda is n over T. And W is the mean of the stays, each departure minus its arrival.

@chapter A trace of five
@words text="arrive 0, 1, 2, 5, 6 · leave 3, 4, 6, 8, 10" sub="T = 10"
Five customers arrive at zero, one, two, five and six, and leave at three, four, six, eight and ten. Nothing is assumed about why they came when they did or how they were served. This is a record, not a model.

@math heading="Count it two ways" items="N(t): 1 2 3 2 1 2 2 2 1 1 → area 17@slot by slot;;stays: 3 + 3 + 4 + 3 + 4 = 17@add up the stays"
Slot by slot, the number inside is one, two, three, two, one, two, two, two, one, one. That's an area of seventeen. Now add up the stays: three, three, four, three, four. Also seventeen.

@art strips-and-bars
Those two seventeens aren't a coincidence, and they aren't a check that might have failed. Each customer adds one to N of t for exactly as long as it's inside. So you can add the region in vertical strips, one per slot, or in horizontal bars, one per customer. Same region, same total.

@chapter The law
@math heading="Divide by T" items="L = 17/10@seventeen tenths;;λ = 5/10 = 1/2@a half;;W = 17/5@seventeen fifths;;λW = (1/2)(17/5) = 17/10 = L  ✓@lambda W"
Divide by T. L is seventeen tenths. Lambda is five over ten, a half. W is seventeen fifths. And lambda W is a half times seventeen fifths, seventeen tenths. Exactly L.

@words text="no Poisson · no steady state · no independence"
The proof used no property of the arrivals or the service. No Poisson, no memorylessness, no steady state, no service order. Only that every stay lies inside the window. If you can count arrivals and time stays, the law is available.

@chapter Where it seems to fail
@math heading="Cut the trace at T = 8" items="L = 15/8 = 1.875@fifteen eighths;;λ = 5/8,  W = 13/4@five eighths;;λW = 65/32 = 2.03125  ✗@sixty five over thirty two"
Now stop the clock at eight, with the last customer still inside. L is fifteen eighths. Lambda is five eighths, but W averages only the four finished stays, thirteen quarters. Lambda W is sixty five over thirty two. The two sides part company.

@art open-window
That's not the law failing. Lambda counted five arrivals while W averaged four stays. Extend the window to ten, and they agree again. Every report of Little's Law not holding is this: a window with work still in flight, or three quantities measured at three different boundaries.

@chapter What it doesn't say
@art no-overlap
With arrivals at zero, two, four, six, eight and departures two later each, exactly one customer is present at every instant. L is one, lambda a half, W two. Here L is the fraction of time the system is busy, rho, seen from the other side.

@art same-mean-different-tail
But W is a mean. It says nothing about the p ninety nine. Two systems with identical L, lambda and W can have entirely different tails.

@art boundary-box
And the same counting works across any boundary you can draw, with lambda the rate that crosses into it: a component, a thread pool, a whole datacentre. Draw the box, then count what crosses it and how long things stay inside.

@chapter Where people slip
@list heading="Common slips" items="Thinking it needs Poisson arrivals@The first|Measuring with work in flight@The second|Three boundaries for three numbers@The third"
The first slip is believing the identity needs Poisson arrivals. The second is measuring over a window with work still in flight. And the third is measuring L inside a thread pool, lambda at the load balancer and W from the client. Those are three different systems, and their numbers have no reason to agree.

@chapter Try it
@words text="arrive 0, 1, 4 · leave 2, 5, 6" sub="T = 6, everyone has left"
Your turn. Three customers arrive at zero, one and four, and leave at two, five and six. The horizon is six, and everyone has left by then. Build the staircase, get the area both ways, and predict L before you divide anything.

@end text="Count the area both ways"
You can type in any trace and see L, lambda and W as exact fractions, on Learn. That's learn dot get er done dot I O.
