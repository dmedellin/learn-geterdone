---
format: long
lesson: queues-and-utilisation/memoryless-waiting
title: Memoryless waiting: from geometric to exponential
thumb: Quiet time is not credit
---

@chapter The question
@title text="Memoryless Waiting" sub="Queues and Utilisation" art=thumb
The bus hasn't come for three minutes, so it must be due soon. If arrivals are memoryless, that's simply false. Let's build the waiting time from something you already know, and see exactly why.

@art time-slots
Chop time into slots of width delta. In each slot, an arrival happens with probability lambda times delta, independently. The waiting time until the first arrival is geometric. And surviving t units of time means surviving t over delta slots in a row with no arrival.

@math heading="Waiting in slots" items="P(T > t) = (1 − λΔ)^(t/Δ)@the chance of still waiting"
So the chance of still waiting after t is one minus lambda delta, to the power t over delta. That's exact, and it's a fraction.

@words text="λ = 1/2 per second · Δ = 1/10 s → λΔ = 1/20" sub="λΔ is a probability; λ is a rate"
Notice that lambda delta is a probability, and lambda isn't. A rate of a half per second, in slots of a tenth of a second, becomes a probability of one in twenty per slot. Halve the slot and that probability halves. The rate doesn't move.

@chapter Shrinking the slot
@math heading="λ = 1/2,  t = 4 s,  λt = 2" items="Δ = 1/10:  (19/20)⁴⁰ = 0.1285122@a tenth;;Δ = 1/100:  (199/200)⁴⁰⁰ = 0.1346580@a hundredth;;Δ → 0:  e^(−2) ≈ 0.1353353@shrink the slot"
With a half per second and four seconds, take slots of a tenth. That's nineteen twentieths to the fortieth, nought point one two eight five one two two. With slots of a hundredth, a hundred and ninety nine over two hundred to the four hundredth, nought point one three four six five eight. Shrink the slot to nothing, and you reach e to the minus two, about nought point one three five three three five three.

@art converging
Each tenfold refinement closes about nine tenths of the remaining gap. The exact column approaches from below, because a slotted clock only lets an arrival happen at a slot boundary, so it gets slightly fewer chances.

@art e-limit
That limit is where e comes from. It's the exponential distribution, arriving as a limit of a geometric tail you already had. No density, no integral. And the exponential figure is computed by summing a series, so it's rounded, while the geometric column is exact.

@chapter Memoryless
@math heading="The memoryless property" items="P(T > s + t | T > s) = P(T > s + t)/P(T > s)@having already waited;;= (1 − λΔ)^((s+t)/Δ) / (1 − λΔ)^(s/Δ)@substitute;;= (1 − λΔ)^(t/Δ) = P(T > t)@the powers subtract"
Now ask: having already waited s, what's the chance you wait t more? It's the tail at s plus t, over the tail at s. Substitute the formula, and the powers subtract. What's left is one minus lambda delta to the t over delta, the plain tail at t. Nothing about s survives.

@art same-tail
Draw the tail of the wait starting from now, or starting after you've already waited a while, and it's the same curve.

@art bus-stop
So if the bus hasn't come for three minutes, the chance it takes another four is the same as when you arrived. Quiet time is not credit. And it holds at every slot size, so it's exact, not something the exponential picks up in the limit.

@art bunching
What memorylessness doesn't claim is that arrivals are evenly spread. It's exactly what makes bunching possible. Nothing discourages two arrivals in consecutive slots, because the process has no record of the first one.

@chapter Longer than the mean
@math heading="The mean wait" items="E[T] = 1/λ = 2 s@one over lambda;;P(T > mean) = e^(−1) ≈ 0.368@e to the minus one"
The mean wait is one over lambda, two seconds at a half per second. But the tail at the mean isn't a half. It's e to the minus one, about nought point three six eight. An exponential wait is longer than its mean about thirty seven percent of the time.

@chapter Where people slip
@list heading="Common slips" items="It hasn't come, so it's due@The first|λ as a per-slot probability@The second|The exponential figure as exact@The third"
The first slip is thinking it hasn't arrived in a while, so it's due. A process with no memory can't owe you anything. The second is treating lambda itself as a per slot probability. Lambda can exceed one. Lambda delta can't. And the third is quoting the exponential figure as exact.

@chapter Try it
@words text="λ = 1 per second · t = 3" sub="λt = 3, so the limit is e^(−3)"
Your turn. Take lambda as one per second and t as three. Then lambda t is three, so the limit is e to the minus three. Before you compute either, predict whether the geometric tail with slots of a tenth lands above or below it.

@end text="No memory, no credit"
You can shrink the slot and watch the geometric tail walk towards the exponential, on Learn. That's learn dot get er done dot I O.
