---
format: long
lesson: replication-and-consistency/vector-clocks-and-concurrency
title: Vector clocks: how to tell that two events are concurrent
thumb: Before, after, or neither
---

@chapter The question
@title text="Vector Clocks and Concurrency" sub="Replication and Consistency" art=thumb
A Lamport clock always says one event is before another, even when nothing connects them. A vector clock can say something a single number never can: these two are unrelated. That's exactly the answer a merge needs.

@art vector-boxes
A vector clock gives each event one counter per process. So with three processes, A, B and C, every stamp is three numbers. Read it as how much of each process's history this event knows about.

@chapter The rule
@math heading="Vector clock" items="own event:  V[i] = V[i] + 1@its own component at each;;receive:  V = max(V, V_msg) elementwise, then V[i] + 1@a receive"
Process i increments its own component at each of its events. A message carries the sender's whole vector. On a receive, take the elementwise maximum with your own, then increment your own component.

@art merge-max
That maximum is the merge. After a receive, an event knows everything its own process knew, plus everything the sender knew. Nothing is ever forgotten, only added.

@art three-processes
Here's the same diagram as the Lamport lesson. Three processes, eleven events, and three messages: A two to B two, B three to C two, and C one to A four.

@math heading="Messages: A2 → B2 · B3 → C2 · C1 → A4" items="B2 = max((0,1,0), (2,0,0)) + B = (2,2,0)@B two;;C2 = max((0,0,1), (2,3,0)) + C = (2,3,2)@C two;;A4 = max((3,0,0), (0,0,1)) + A = (4,0,1)@A four"
B two takes the max of zero one zero and two zero zero, then bumps B: two, two, zero. C two takes the max with two, three, zero, then bumps C: two, three, two. And A four becomes four, zero, one.

@words text="C3 = (2,3,3)" sub="knows A's first 2, B's first 3, and is C's 3rd"
Read C three, two three three, as a sentence. This event knows about the first two events of A, the first three of B, and it's C's own third.

@chapter Comparing vectors
@math heading="Happens-before, decided" items="e → f  ⟺  V(e) ≤ V(f) componentwise and V(e) ≠ V(f)@if and only if;;neither dominates  ⟺  concurrent@neither"
Now e happened before f if and only if every component of e's vector is at most f's, and they differ. And if neither vector dominates the other, the events are concurrent. That if and only if is what a Lamport stamp couldn't offer.

@math heading="Two comparisons" items="A2 (2,0,0) vs B1 (0,1,0):  2 ≤ 0 no · 1 ≤ 0 no  →  concurrent@A two;;A1 (1,0,0) vs C3 (2,3,3):  1 ≤ 2, 0 ≤ 3, 0 ≤ 3  →  A1 → C3@A one"
A two against B one. Is two at most zero? No. Is one at most zero? No. Neither dominates, so they're concurrent. A one against C three. One at most two, zero at most three, zero at most three. So A one happened before C three.

@art refuses
A single integer can always be compared, so it always gives an answer, even when there's none to give. A vector can simply refuse to compare. That refusal is the answer.

@chapter The census
@list heading="All pairs of the 11 events" items="C(11,2) = 55 pairs@fifty five|32 ordered@thirty two|23 concurrent, 41.8%@twenty three"
Eleven events make fifty five pairs. Thirty two are ordered. Twenty three are concurrent, nearly forty two percent. And seventeen of the pairs Lamport ordered are among those twenty three.

@art sparse-messages
That's not an anomaly. Concurrency is the default, and ordering is what communication buys. A system that gossips rarely has many concurrent pairs. One that synchronises constantly has few, and pays in messages.

@chapter Concurrent is not simultaneous
@math heading="A3 vs C3" items="A3 (3,0,0) ≤ C3 (2,3,3)?  3 ≤ 2 no@does A three;;C3 ≤ A3?  3 ≤ 0 no@does C three;;concurrent@concurrent"
A three is three, zero, zero. C three is two, three, three. Does A three precede C three? Three isn't at most two. Does C three precede A three? Three isn't at most zero. Concurrent.

@art wall-clock
But C three is the last event on its process, and A three is mid way along another. On a wall clock, they could be minutes apart. The vectors aren't saying they happened at the same moment. They say neither process could have known of the other's event. That's when two updates conflict.

@chapter Where people slip
@list heading="Common slips" items="Reading concurrent as simultaneous@The first|Comparing vectors by sum or one component@The second|Expecting the vector to pick the right update@The third"
The first slip is reading concurrent as simultaneous. The second is comparing vectors by their sum, or one component. A three sums to three and C three to eight, but they're concurrent. The third is expecting the vector to say which concurrent update is right. It just says they conflict.

@chapter Try it
@words text="delete the message C1 → A4" sub="A4 becomes (4,0,0)"
Your turn. Delete the message from C one to A four. A four becomes a local event, four, zero, zero. Restamp what changes, predict whether the concurrent count rises or falls, then compute it.

@end text="Stamp with vectors, count the conflicts"
You can stamp a diagram with vectors and count every concurrent pair, on Learn. That's learn dot get er done dot I O.
