---
format: short
lesson: replication-and-consistency/lamport-clocks
title: A smaller Lamport timestamp doesn't mean it happened first
---

@art chain-increases
If event a caused event b, a's Lamport stamp is smaller. But the reverse isn't true.

@math items="L(B1) = 1 < 2 = L(A2)@one is less than two;;no chain from B1 to A2@no chain"
Here, B one has stamp one and A two has stamp two. One is less than two. But no chain of messages runs from B one to A two. They're concurrent.

@words text="Sound, not complete"
A Lamport clock never orders an effect before its cause. It just can't tell you two events were unrelated.

@end text="Full lesson on Learn"
The full lesson, with a diagram to stamp, is on Learn.
