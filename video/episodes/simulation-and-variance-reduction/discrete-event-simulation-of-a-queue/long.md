---
format: long
lesson: simulation-and-variance-reduction/discrete-event-simulation-of-a-queue
title: Discrete-event simulation of a queue, event by event
thumb: Jump to the next event
---

@chapter The calendar is the model
@title text="Discrete-Event Simulation of a Queue" sub="Simulation and Variance Reduction" art=thumb
How do you simulate a queue? You don't tick the clock one moment at a time. You jump straight to the next thing that happens.

@art event-calendar
A discrete event simulation has three parts: the current state, a calendar of events scheduled for the future, and a clock. Each step takes the earliest event, moves the clock to it, applies its effect, and schedules whatever the new state implies.

@art clock-jumps
So the clock jumps. Every instant where nothing happens is skipped, never visited at all.

@chapter The model
@words text="arrival p = 2/5 · service ends q = 1/2" sub="per slot · single server"
The model is the single server queue solved exactly earlier in the course. In each slot, an arrival happens with probability two fifths, and a customer in service finishes with probability a half. Both are sampled by inverse transform from the seeded stream, so every figure is a fraction.

@chapter One run, event by event
@words text="Arrivals: 3, 5, 6, 7, 8" sub="customer 1 leaves at 4 · customer 2 serves 3 slots"
Seed one. Customer one arrives at slot three, and leaves at four. Customer two arrives at five, needing three slots. Customers three and four arrive at six and seven, and queue behind it. Nothing happens at slots zero, one or two, and the clock never visits them.

@art tie-instant
At clock eight, two events share the instant: customer two departs, and customer five arrives. The rule: departures first. So right after the departure the system holds two, and the arrival takes it to three.

@words text="Departures before arrivals" sub="stated once, obeyed everywhere"
That's not a detail. Ask who's in the system by testing arrival before t before departure, and you'd count the new arrival during the departure. Your headcount would disagree with your own list of names. So walk the event list, and the count and contents are the same thing.

@chapter Time averages
@art step-function
The number in the system is a step function. Its time average is the area under it, divided by the length of the window. Not the average of the values it took, but weighted by how long it took them.

@art weighted-average
One customer for nine hundred slots and nine for a hundred: the time average is one point eight. The plain average of the two states is five. Only the first is what anyone wants.

@chapter The long run
@math heading="2000 slots, seed 1" items="exact:  L = 12/5 = 2.4,  ρ = 4/5@exact;;776 customers · area 4733@seven hundred seventy six;;time average 4733/2000 = 2.3665@time average;;server busy 1593/2000 = 79.7%@busy"
The exact answer, from the chain, is twelve fifths, two point four. Two thousand slots give seven hundred seventy six customers and an area of four thousand seven hundred thirty three. So the time average is two point three six six five. The server is busy seventy nine point seven percent of the time.

@art reseeded-runs
The gap, about point oh three, isn't a rounding error. There's no rounding in it. It's one draw of a random quantity. Reseed, and it moves: one point nine six six, two point seven three, two point five three. Report only one, and you're reporting a coincidence.

@chapter Little's law in one run
@words text="L = λW" sub="an identity about one run's own averages"
The area under the curve is also the sum of every customer's time in the system. Divide it by the horizon for the time average. Divide it by the customers for the mean time in the system. They're related by L equals lambda W, as pure arithmetic.

@words text="4733/2005 vs 4733/2000"
Just be consistent about the horizon. The trace runs to the last departure at slot two thousand and five, while the panel divides by two thousand. Same area, two denominators, and the identity holds for either one.

@chapter Where people slip
@list heading="Common slips" items="Recomputing the state from the clock@The first|Reporting a single run@The second|Mixing the time average with the per-customer average@And the third"
The first slip is recomputing the state from the clock instead of walking the events. The second is reporting a single run as the answer. And the third is confusing the time average of the number in system with the average time per customer.

@chapter Try it
@words text="Seed 1 · first ten events"
Your turn. Write out the first ten events of seed one in a table: clock, event, and number in system after it. Check that at clock eight you get two, then three.

@end text="Walk the calendar"
You can step through the queue event by event, and reseed it, on Learn. That's learn dot get er done dot I O.
