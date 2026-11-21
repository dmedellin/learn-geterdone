---
format: long
lesson: queues-and-utilisation/why-queues-form-below-full-utilisation
title: Why queues form below full utilisation
thumb: Bunching, not overload
---

@chapter The question
@title text="Why Queues Form at ρ < 1" sub="Queues and Utilisation" art=thumb
We're only at seventy percent, so nobody should be waiting. That sentence is true of exactly one kind of system: one where work arrives on a timetable and takes the same time every time. Everywhere else, work waits well below full utilisation.

@chapter Clockwork
@art clockwork
Start with clockwork at rho of four fifths. One arrival every five slots, and each takes exactly four slots to serve. The server finishes before the next arrival appears. So the system holds one customer four slots in five, and none in the fifth.

@math heading="Clockwork, ρ = 4/5" items="L = 4/5@four fifths;;most ever present = 1@the largest"
The mean number in the system is four fifths: the one in service, counted for the fraction of time it's there. And the largest number ever present is one. Below one, a deterministic system never queues at all.

@chapter Randomness
@art slotted-model
Now make it random. Time moves in slots. In each slot, an arrival happens with probability p. A customer in service finishes with probability q each slot, so service times are geometric, with a mean of one over q slots. Departures are resolved before arrivals within a slot.

@math heading="Same utilisation" items="p = 2/5,  q = 1/2@two fifths;;ρ = p/q = (2/5)/(1/2) = 4/5@the same;;mean service = 2 slots@two slots"
Take p of two fifths and q of a half. Rho is p over q, two fifths over a half, which is four fifths. The same utilisation as the clockwork run, the same mean service time of two slots, and the same throughput.

@math heading="The exact chain" items="L = p(1 − p)/(q − p)@a closed form;;= (2/5)(3/5)/(1/10) = 12/5 = 2.4@twelve fifths;;12/5 ÷ 4/5 = 3@three times"
This chain has a closed form, derived in Operations Research: L is p times one minus p, over q minus p. That's two fifths times three fifths, over a tenth, which is twelve fifths. Three times the clockwork answer, at identical utilisation.

@art bunching-arrivals
The server is idle exactly as often as before. It's just idle at the wrong moments. Arrivals bunch, and the work that lands while the server is busy is what waits. Bunching, not overload.

@art two-queues
So put the two side by side. The arrival rate, the mean service time, the utilisation and the throughput are all identical. What differs is when arrivals land and how long each service actually takes. And that alone gives twelve fifths instead of four fifths.

@words text="idle 30% of the time · but when?"
The honest version of the opening sentence: at seventy percent utilisation the server is idle thirty percent of the time, and whether anyone waits depends on how that idleness is spread out. Randomness spreads it badly.

@chapter Not M/M/1
@math heading="A different model" items="ρ/(1 − ρ) = (4/5)/(1/5) = 4@four;;4 ÷ 12/5 = 5/3@five thirds"
You might reach for the continuous formula, rho over one minus rho. At four fifths that's four. But four isn't this system's answer. It overstates the exact twelve fifths by five thirds. The two agree only as the slot shrinks to nothing, which is the subject of the M M one lesson.

@chapter The simulation starts empty
@art warm-up
The lab runs this as a simulation, and a run begins with nothing in the system, a state the settled chain visits only a fifth of the time. So averaging from time zero comes out biased low. The lab prints the mean twice: from the start, and after discarding a warm up.

@art seed-runs
And neither printed mean is the exact answer. One run is a sample, and a different seed gives a different number. What's stable across seeds is the comparison: the random arm above the clockwork arm, by a factor near three.

@chapter Where people slip
@list heading="Common slips" items="At 70% nobody waits@The first|A simulated mean as exact@The second|Expecting ρ/(1 − ρ) here@The third"
The first slip is believing nobody waits at seventy percent. There's no threshold where waiting begins. The second is reading a simulated mean as the exact answer. And the third is expecting this simulation to produce rho over one minus rho. A run that did would mean the simulator was wrong.

@chapter Try it
@words text="p = 1/4 · q = 1/2" sub="ρ = 1/2"
Your turn. Set p to a quarter and q to a half, so rho is a half. Predict whether the gap between the random and clockwork arms is larger or smaller than it was at four fifths. Then run it and see.

@end text="Idle time, at the wrong moments"
You can run the clockwork and the random queue side by side, on Learn. That's learn dot get er done dot I O.
