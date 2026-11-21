---
format: long
lesson: markov-chains-decisions-and-queues/communicating-classes-recurrence-and-period
title: Communicating classes, recurrence and period, read off the arcs
thumb: An arc is an arc
---

@chapter Structure from arcs
@title text="Communicating Classes, Recurrence and Period" sub="Markov Chains, Decisions and Queues" art=thumb
Before you ask where a Markov chain settles, ask three structural questions. Who can reach whom? What can the chain never leave? And does it move in a rhythm? All three come from the arcs, not the probabilities.

@chapter Classes
@math heading="Reachability" items="i → j  when Pⁿ[i][j] > 0 for some n ≥ 0@reachable;;i ↔ j  when i → j and j → i@communicate"
State j is reachable from i when some power of P has a positive i, j entry. And i and j communicate when each can reach the other.

@art class-blobs
Communicating is an equivalence relation, so it splits the states into classes, with no overlaps and nothing left over. The chain is irreducible when there's exactly one class, so everything reaches everything.

@words text="↔ · → · ·" sub="the reachability table"
The lab computes reachability as the transitive closure of the arcs, covering every path. Each cell of its table shows a two way arrow when the states reach each other, a one way arrow when only one direction works, and a dot when neither does. The two way cells are exactly the pairs that share a class.

@chapter Recurrent or transient
@art transient-escape
A class is recurrent, or closed, when no arc leaves it. Otherwise it's transient. Here's why. If an arc leads out and never comes back, every visit to its tail takes it with some fixed chance. Over infinitely many visits, the chance of never taking it is zero. So the chain leaves, for good.

@art thin-arc-out
Notice nothing used a size. An arc of one in a thousand out of a class decides it just like one of a half. The chain leaves every time, eventually. A small arc changes how long it takes, not whether.

@words text="1/2 1/4 1/4 ; 0 3/4 1/4 ; 0 1/2 1/2" sub="classes {trial} and {kept, lapsed}"
The lesson's example has three states: trial, kept and lapsed. Nothing returns to trial, so it's transient. Kept and lapsed form a closed class. Its stationary distribution is zero, two thirds, one third, and that zero is exact.

@chapter The period
@math heading="Period" items="d(i) = gcd{ n ≥ 1 : Pⁿ[i][i] > 0 }@greatest common divisor"
The period of a state is the greatest common divisor of the lengths of its closed walks back to itself. States in one class share a period. A period of one means aperiodic, and any self loop forces that immediately.

@art three-cycle
A three state ring with no other arcs has walks of length three, six, nine, and so on. Period three. It returns to where it started only at multiples of three, forever.

@art bfs-levels
And you don't need to list cycles. Level the class with a breadth first search. Then take the greatest common divisor, over every arc u to v inside the class, of the level of u, plus one, minus the level of v.

@math heading="The ring, levelled" items="1 → 2:  0 + 1 − 1 = 0@one to two;;2 → 3:  1 + 1 − 2 = 0@two to three;;3 → 1:  2 + 1 − 0 = 3@three to one;;gcd(0, 0, 3) = 3@greatest"
Levels are zero, one and two. One to two gives zero. Two to three gives zero. Three to one gives two plus one minus zero, three. The greatest common divisor is three, and no cycle was ever written down.

@chapter Both hypotheses
@words text="Irreducible + aperiodic ⇒ Pⁿ → π" sub="stated, not proved"
Here's why this matters. If a finite chain is irreducible and aperiodic, its powers converge to the unique steady state. The course states that and doesn't prove it. But you can check both hypotheses on any matrix.

@art two-closed-groups
And you need both. The ring is irreducible but periodic, so its powers cycle forever. This four state chain has two closed groups. It's aperiodic but reducible, so the balance equations have a whole family of solutions, not one.

@chapter Where people slip
@list heading="Common slips" items="Treating a small escape as no escape@The first|Calling it aperiodic because no rhythm was noticed@The second|Thinking irreducible means aperiodic@And the third"
The first slip is treating a small escape probability as no escape. The second is calling a chain aperiodic because no rhythm was noticed. Walks of four, six and ten give period two. And the third is thinking irreducible and aperiodic are the same. They're independent.

@chapter Try it
@words text="1/2 1/2 0 0 ; 1/2 1/2 0 0 ; 0 0 1/3 2/3 ; 0 0 1/4 3/4"
Your turn. For this four state chain, build the reachability table, list the classes, decide which are recurrent, and compute each period. Then explain why there's no single steady state.

@end text="Read the structure off the arcs"
You can type any matrix and see its classes, recurrence and period, on Learn. That's learn dot get er done dot I O.
