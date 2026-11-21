---
format: long
lesson: replication-and-consistency/lamport-clocks
title: Lamport clocks: a smaller timestamp doesn't mean earlier
thumb: Sound, not complete
---

@chapter The question
@title text="Lamport Clocks" sub="Replication and Consistency" art=thumb
Distributed machines can't agree on the time. So how do you order their events? A Lamport clock is one counter and one rule. It gets one direction exactly right, and the other direction badly wrong.

@art space-time
Event a happens before b if they're on the same process and a is earlier, or a is the send of a message whose receive is b, or there's a chain of those steps from a to b. Events with no such chain are unrelated. That's a partial order, not a total one.

@chapter The rule
@math heading="The Lamport timestamp" items="local event:  L = L + 1@a local event;;send:  L = L + 1, attach L@a send;;receive:  L(e) = max(L_local, L_msg) + 1@a receive"
Each process keeps one integer. On a local event, add one. On a send, add one and attach the value to the message. On a receive, take the maximum of your own counter and the message's, then add one.

@words text="max carries information · + 1 keeps receive after send"
The maximum is what carries information across processes. The plus one keeps every receive strictly after its send.

@chapter Eleven events
@list heading="Messages: A2 → B2 · B3 → C2 · C1 → A4" items="A:  1, 2, 3, 4@process A|B:  1, 3, 4, 5@process B|C:  1, 5, 6@process C"
Three processes. Messages go from A two to B two, B three to C two, and C one to A four. Process A stamps one, two, three, four. Process B, one, three, four, five. Process C, one, five, six.

@math heading="The three receives" items="B2 = max(1, 2) + 1 = 3@B two;;C2 = max(1, 4) + 1 = 5@C two;;A4 = max(3, 1) + 1 = 4@A four"
B two is the max of one and two, plus one, three. C two is the max of one and four, plus one, five. And A four is the max of three and one, plus one, four.

@art local-wins
That third one is instructive. The message from C one carries a one, smaller than A's own counter. So the local clock wins, and A four is four, not two. Adding one to the message's stamp instead would make A's own stamps go backwards. Check each process line increases.

@chapter Sound
@art chain-increases
If a happened before b, every step of the chain strictly increases the stamp. So L of a is less than L of b. That's sound. Break ties by process name, and you get a total order that never puts an effect before its cause.

@chapter Not complete
@math heading="The converse fails" items="L(B1) = 1 < 2 = L(A2)@L of B one is one;;B1 → B2 → B3 → C2 → C3, and C3 sends nothing@Is there a chain;;no chain from B1 to A2: concurrent@concurrent"
But the converse is false. L of B one is one, less than L of A two, which is two. Is there a chain from B one to A two? B's chain leads to C two and C three, and C three sends nothing. The only message into A comes from C one, which B can't reach. So they're concurrent.

@art false-pair
On this diagram, thirty two pairs are ordered by happens before. And seventeen further pairs have a smaller stamp with no causal order at all. That's not a rare corner case. A single integer can't say these two are unrelated.

@chapter What it's for
@art total-queue
A total order everyone agrees on is still useful. A distributed mutual exclusion queue. A deterministic replay of a log. What it can't do is detect that two updates were concurrent. A merge that trusts it will silently pick a winner between two updates that should both have been kept.

@art one-counter
One integer per process is all a Lamport clock costs, and it's all it can carry. The next lesson spends one counter per process, in every stamp, and gets the missing direction back.

@chapter Where people slip
@list heading="Common slips" items="Reading a smaller stamp as earlier@The first|Incrementing the message's stamp, not the max@The second|Expecting Lamport stamps to detect conflicts@The third"
The first slip is reading a smaller stamp as earlier. It only means b didn't happen before a. The second is incrementing the message's stamp instead of the maximum. The third is expecting Lamport stamps to detect a conflict. By construction, they can't.

@chapter Try it
@words text="add a message A3 → C3" sub="C3 = max(L(C2), L(A3)) + 1"
Your turn. Add a fourth message, from A three to C three. Now C three is a receive, so its stamp is the max of C two and A three, plus one. Restamp anything that changes, and say whether the number of false pairs should rise or fall, and why.

@end text="Stamp a diagram, find the false pairs"
You can stamp a message diagram and see which ordered stamps have no causal chain behind them, on Learn. That's learn dot get er done dot I O.
