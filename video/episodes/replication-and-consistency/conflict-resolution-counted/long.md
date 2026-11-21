---
format: long
lesson: replication-and-consistency/conflict-resolution-counted
title: Last-writer-wins vs a counter CRDT, counted on one trace
thumb: Better clocks lose the same
---

@chapter The question
@title text="Conflict Resolution, Counted" sub="Replication and Consistency" art=thumb
Three replicas take writes during a partition. The partition heals and they merge. How many acknowledged updates just vanished? With last writer wins, you can count them. And better clocks won't change the count.

@art partitioned
Updates are concurrent when no chain of messages orders them. That's the condition vector clocks make decidable. A merge has to turn conflicting states into one answer. The question is what each rule throws away to get there.

@chapter Two rules
@list heading="Merge rules" items="Last-writer-wins: keep the replica with the largest timestamp@Last writer wins|Counter CRDT: one count per replica, merge by max, sum@A counter"
Last writer wins keeps the state of the replica holding the largest timestamp. A counter CRDT keeps one count per replica, merges two states by elementwise maximum, and reports the sum.

@chapter One trace
@math heading="Replica : timestamp : delta" items="A:3:+2 · B:5:+3 · C:4:+1 · B:9:+4@the trace;;true total = 2 + 3 + 1 + 4 = 10@the true total"
Here's the trace. A at time three adds two. B at five adds three. C at four adds one. And B at nine adds four. No replica has seen any other's update. Every one was acknowledged to a client. The true total is ten.

@math heading="Last-writer-wins" items="largest timestamp 9, held by B@nine;;B's register = 3 + 4 = 7@three plus four;;discarded: A's +2, C's +1  →  2 updates, worth 3@discarded"
The largest timestamp is nine, held by B. So B's register wins, and it contains only B's own updates, three plus four, seven. A's plus two and C's plus one are discarded. Two updates, worth three.

@art silent-drop
No error is raised anywhere. A reader sees seven for increments totalling ten. That's not a bug in the implementation. It's what the rule says to do. And it's the default in a great deal of software.

@math heading="Counter CRDT" items="A = 2 · B = 3 + 4 = 7 · C = 1@a component per replica;;merge: elementwise maximum@merge;;value = 2 + 7 + 1 = 10 · discarded 0@ten"
The counter keeps a component per replica. A is two, B is seven, C is one. Merge by elementwise maximum, in any order. The value is two plus seven plus one, ten. Nothing discarded. Ten against seven, from the same trace and the same acknowledgements.

@chapter The clocks aren't the problem
@art exact-clocks
The reflex fix is to make the timestamps accurate. Make them exact to the nanosecond. The rule still keeps one replica's register and discards the rest. The winner may change, but two updates are still lost. These updates weren't ordered, so there was no order to be precise about.

@art component-vector
The deeper problem is that last writer wins treats an increment as a state to overwrite. Once plus two has become A's register reads two, the only way to combine it with B's seven is to choose. The counter never merges them into one slot. Each replica only ever increments its own component, so nothing it did can be overwritten by anyone else.

@chapter Why the merge converges
@list heading="Elementwise maximum is" items="commutative@commutative|associative@associative|idempotent@idempotent"
Elementwise maximum has three laws. It's commutative, so gossip order doesn't matter. It's associative, so how exchanges are grouped doesn't matter. And it's idempotent, so a redelivered message doesn't double count.

@art converge
Drop any one, and replicas disagree forever, or count twice. With all three, every replica converges with no coordination at all. No ordering, no exactly once delivery, no leader.

@art harder-types
But a grow only counter is the easy case, an existence proof. Sets with removals, documents and ordered lists need more machinery. Some conflicts, like two withdrawals from one balance, are business decisions no merge should quietly make. The transferable question is: what does my rule discard, and can I count it?

@chapter Where people slip
@list heading="Common slips" items="Believing better clocks make LWW safe@The first|Reporting only one of the two counts@The second|Generalising the counter to every data type@The third"
The first slip is believing better clocks make last writer wins safe. The second is reporting only one of the two counts. Two updates discarded and worth three answer different questions. The third is generalising the counter to every data type.

@chapter Try it
@words text="add A:11:+5" sub="largest timestamp now 11, held by A"
Your turn. Add a fifth update: A at eleven adds five. Now A holds the largest timestamp, so A's register wins. Find the new last writer wins value, how many updates it discards and their worth, and the CRDT's value. Did the number discarded go up or down?

@end text="Merge a trace both ways"
You can build a trace of concurrent updates and count what each merge throws away, on Learn. That's learn dot get er done dot I O.
