---
format: long
lesson: intro-algorithms-algebraic-topics/multithreaded-algorithms
title: Work, span and parallelism: when more processors help
thumb: The span sets the floor
---

@chapter Leaving the serial model
@title text="Multithreaded Algorithms" sub="Introduction to Algorithms, Chapter 27" art=thumb
Chapter twenty seven begins by stepping outside the model the rest of the book uses.

@quote text="The vast majority of algorithms in this book are serial algorithms suitable for running on a uniprocessor computer in which only one instruction executes at a time." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 27"
The vast majority of algorithms in this book are serial algorithms suitable for running on a uniprocessor computer in which only one instruction executes at a time.

@list heading="Three keywords" items="spawn: the caller goes on while the child runs@Spawn|sync: wait for every spawned child@sync|parallel: loop iterations may run at once@parallel"
The model adds three keywords. Spawn lets the caller go on while the child runs. Sync makes it wait for every child it spawned. And parallel, in front of a for loop, says the iterations may run at once. Delete the three words, and you get an ordinary serial program that computes the same thing.

@chapter Work and span
@art strand-dag
A run of such a program is a directed acyclic graph. Each vertex is a strand, a run of instructions with no parallel control. Each edge says which must finish first.

@math heading="Two numbers" items="work T₁: total cost of all strands@the work;;span T∞: cost of the costliest path@the span"
Two numbers describe the graph. The work, T one, is the total cost of the strands, the time on one processor. The span, T infinity, is the cost of the costliest path, the time with unboundedly many.

@math heading="Two laws" items="work law: T_P ≥ T₁/P@work law;;span law: T_P ≥ T∞@span law;;speedup ≤ T₁/T∞, the parallelism@parallelism"
The work law: in one step, P processors do at most P units of work, so T P is at least T one over P. The span law: P processors can't beat unboundedly many, so T P is at least T infinity. The speedup is capped by the parallelism, T one over T infinity.

@chapter The greedy scheduler
@art greedy-steps
A greedy scheduler never leaves a processor idle when a strand is ready. A complete step keeps all P busy, and there are at most T one over P of those. An incomplete step runs every ready strand, so it shortens the remaining span by one. At most T infinity of those.

@words text="T_P ≤ T₁/P + T∞" sub="Theorem 27.1 · never worse than twice optimal"
Add the two counts, and that's theorem twenty seven point one. Since the optimum is at least the larger of the two terms, greedy never takes more than twice the best schedule.

@chapter Seven strands by hand
@math heading="init 2 · load 6 · parse 3 · index 4 · check 2 · merge 1 · done 1" items="work = 19@The work is;;init, load, done = 9@two plus six plus one;;init, parse, index, merge, done = 11 = span@The span is;;P = 2: greedy ≤ 20.5 · no schedule beats 11@On two processors"
Here's a small program of seven strands. The work is nineteen. One path, init, load, done, costs two plus six plus one, nine. The other costs eleven. The span is eleven, and the parallelism about one point seven three. On two processors, the greedy bound is twenty point five, and no schedule beats eleven.

@chapter P-FIB and merge sort
@math heading="P-FIB" items="pfib-10: T₁ = 353 · T∞ = 20 · parallelism 17.65@the work is three fifty three;;pfib-25: parallelism 9,711.38 on 64 processors@twenty five"
P fib spawns its first recursive call. For n equals ten, the work is three fifty three and the span twenty, a parallelism of seventeen point six five. For n equals twenty five on sixty four processors, the parallelism is over nine thousand seven hundred, and the greedy bound is within one percent of the lower bound.

@art serial-merge
Merge sort is different. Spawn the two halves but merge serially, and the merge sits on the critical path at the top. On a thousand and twenty four keys, the span is two thousand forty seven, and the parallelism only about five and a half.

@math heading="1,024 keys" items="8 processors: ≤ 3,455@eight;;64 processors: ≤ 2,223 · floor 2,047@sixty four"
Going from eight processors to sixty four lowers the greedy bound only from three thousand four hundred fifty five, to two thousand two hundred twenty three. Eight times the processors buys about a third off.

@art span-floor
The serial merge at the top costs a thousand and twenty four on its own, and nothing can go below the span. Past the parallelism, processors sit idle.

@art parallel-merge
The fix is to split the merge itself. P merge takes the median of the larger input, binary searches for it in the smaller one, and merges the two sides in parallel. Its span is theta of log squared n, and the whole sort's parallelism becomes n over log squared n.

@chapter Where people slip
@list heading="Common slips" items="Every extra processor helps@The first|Parallel code does less work@The second|Parallel strands sharing a variable@the third"
The first slip is expecting every extra processor to help. The second is thinking parallel code does less work. It doesn't. Only the span changes. And the third is letting parallel strands share a variable.

@art race
That's a determinacy race: two parallel strands touch one location, and at least one writes. The answer depends on the schedule, and a race can pass every test run, then fail on the next. Keep parallel strands independent.

@chapter Try it
@words text="P-FIB(6) · MERGE-SORT′ on 16 keys" sub="work and span by hand"
Your turn. Compute the work and span of P fib of six from those of four and five, and of merge sort on sixteen keys. Then find the smallest n where P fib has a slackness of ten on sixty four processors.

@end text="Find the span"
You can compute work, span and the greedy bound yourself, on Learn. That's learn dot get er done dot I O.
