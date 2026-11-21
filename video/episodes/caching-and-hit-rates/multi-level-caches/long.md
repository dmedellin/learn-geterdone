---
format: long
lesson: caching-and-hit-rates/multi-level-caches
title: Two cache levels: why the hit rates multiply, not add
thumb: The misses multiply
---

@chapter The question
@title text="Multi-level Caches" sub="Caching and Hit Rates" art=thumb
Your first cache hits eighty percent. Your second hits fifty. So together they hit a hundred and thirty percent? Obviously not. But the same mistake with smaller numbers looks perfectly reasonable, and that's the one to catch.

@art two-levels
A request is served by level one with probability h one. If it misses, it tries level two. If it misses both, it goes to the origin. And level two only ever sees what level one missed.

@chapter A conditional rate
@math heading="What h₂ means" items="h₂ = P(L2 hit | L1 miss)@the probability of;;measured on the L1 misses only@measured on"
So h two isn't a number about all requests. It's the probability of an L two hit, given an L one miss. It's measured on a different population, the requests that reached it.

@words text="E[X | B]" sub="the expectation over only the outcomes where B happened"
That's a conditional expectation. The expectation of X over only the outcomes where B happened, renormalised by the probability of B. Here, B is missed level one, and there are only three outcomes, so you can list them by hand.

@chapter The misses multiply
@math heading="h₁ = 80%, h₂ = 50%" items="global miss = (1 − h₁)(1 − h₂)@reaches the origin;;= (1/5)(1/2) = 1/10@a fifth times a half;;global hit = 9/10 = 90.00%@ninety percent"
A request reaches the origin only if it missed both. So the global miss rate is one minus h one, times one minus h two. A fifth times a half is a tenth. The global hit rate is nine tenths, ninety percent.

@art misses-multiply
Think of two sieves. The second one only catches what fell through the first. So you multiply the fractions that get through. Adding the catches double counts, which is how you end up at a hundred and thirty percent.

@chapter Three outcomes
@art three-paths
Now latency. Every request pays the level one lookup, one millisecond. The ones that miss pay five more for level two. The ones that miss both pay fifty more for the origin. So the origin path costs fifty six, not fifty.

@math heading="t = 1, 5, 50 ms" items="L1 hit:  4/5 × 1 ms = 4/5@four fifths;;L1 miss, L2 hit:  1/10 × 6 ms = 3/5@a tenth times six;;both miss:  1/10 × 56 ms = 28/5@fifty six;;4/5 + 1/10 + 1/10 = 1 ✓@sum to one;;mean = 35/5 = 7 ms@seven milliseconds"
Four fifths hit level one, at one millisecond, contributing four fifths. A tenth times six gives three fifths. A tenth times fifty six gives twenty eight fifths. The probabilities sum to one, and the contributions add to thirty five fifths, seven milliseconds.

@math heading="Forwards" items="t₁ + (1 − h₁)(t₂ + (1 − h₂)t₃)@read the branch forwards;;= 1 + (1/5)(5 + (1/2)(50))@one plus;;= 1 + 6 = 7 ms@one plus six"
Or read the branch forwards. One, plus a fifth of five plus half of fifty. That's one plus six, seven milliseconds. Same answer. If your probability column doesn't sum to one, you've used a conditional rate as an unconditional one.

@chapter Two wrong answers
@art population-swap
The first wrong answer is adding the rates. At forty and fifty, adding gives a plausible ninety, but the truth is seventy. The second is reading level two's rate as global. L two serving half our traffic? It serves half the misses, a tenth of everything.

@chapter What a level is worth
@art overhead-level
Set h two to zero, a level that never hits. A fifth of requests reach the origin, and the mean is twelve milliseconds. Raise it to fifty percent, and the origin share halves to ten percent and the mean falls to seven. A level that rarely hits adds its lookup to every miss above it.

@words text="worth it when h₂ · t₃ > t₂" sub="50% · 50 ms > 5 ms"
So a level is worth having when h two times t three beats t two. At fifty percent, fifty milliseconds and five, it comfortably does.

@art popular-absorbed
One assumption to name. The requests reaching level two aren't a random sample. They're the unpopular keys, because the popular ones were absorbed above. That's why a second level's hit rate is usually much lower than the first's.

@chapter Where people slip
@list heading="Common slips" items="Adding the two hit rates@The first|Reading L2's rate as a share of all traffic@The second|Averaging the latencies instead of accumulating@The third"
The first slip is adding the two hit rates. The second is reading level two's measured rate as a share of all traffic. The third is averaging the three latencies instead of accumulating them. Write the three path totals first, then weight them.

@chapter Try it
@words text="h₁ = 90% · h₂ = 50% · t = 1, 5, 50 ms" sub="global miss = (1/10)(1/2)"
Your turn. Ninety percent at level one, fifty at level two, the same latencies. The global miss rate starts as a tenth times a half. Finish it, list the three outcomes, compute the mean both ways, and say what share of all requests level two really serves.

@end text="See each branch as a share of all requests"
You can watch both wrong answers printed beside the right one, on Learn. That's learn dot get er done dot I O.
