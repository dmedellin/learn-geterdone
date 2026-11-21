---
format: long
lesson: replication-and-consistency/linearizability-by-enumeration
title: Linearizability by enumeration: every read was right, and the history is wrong
thumb: Zero legal orders
---

@chapter The question
@title text="Linearizability by Enumeration" sub="Replication and Consistency" art=thumb
Every read in this history returned a value the register really held. And the system is still wrong. How do you prove that, rather than just assert it? You count.

@art intervals
Each operation occupies an interval, from when the client issues it to when the response arrives. It can take effect at any single instant inside that interval. Two overlapping operations can go in either order. Two that don't overlap can't.

@chapter The definition
@list heading="A linearization is a total order that is" items="real-time respecting: a ends before b starts  ⟹  a first@real time|legal: every read returns the last written value@legal"
A linearization is a total order of the operations with two properties. It respects real time: if a ended before b started, a comes first. And it's legal: replay it against the object, and every read returns the value last written.

@words text="Linearizable  ⟺  at least one linearization exists"
A history is linearizable if at least one such order exists. That's an existence claim, so enumeration decides it. Generate every order, apply both filters, and count. Zero means no.

@chapter Three operations
@math heading="Register starts at 0" items="A:  write 1  [0, 4]@A writes;;B:  read → 1  [2, 6]@B reads;;C:  read → 0  [5, 9]@C reads;;A ends at 4, C starts at 5  ⟹  A before C@A ends at four"
The register starts at zero. A writes one, from time zero to four. B reads one, from two to six. C reads zero, from five to nine. A ends at four and C starts at five, so A must come before C. Nothing else is forced.

@art per-op-check
Look at each response alone and nothing's wrong. B read one, which was written. C read zero, the initial value. A checker that inspected each response would report no problem at all.

@art forced-pair
So the verdict has to come from the forced pair. A had already returned when C was issued. Whatever instant C took effect at, it was after the write took effect, and yet it returned the value from before the write. Reordering the two overlapping reads can't change that.

@chapter Six orders
@math heading="3! = 6 total orders" items="A B C:  w1, r→1 ✓, r→0 ✗@A B C;;A C B:  w1, r→0 ✗@A C B;;B A C:  r→1 ✗  nothing written yet@B A C;;B C A · C A B · C B A:  C before A, rejected@the other three"
A, B, C: the write, then B reads one, fine, then C reads zero after the write. Illegal. A, C, B: C reads zero right after the write. Illegal. B, A, C: B reads one before anything's written. Illegal. And the other three put C before A, which real time forbids.

@art zero-survivors
Six orders, three allowed by real time, zero legal. The history is not linearizable. C reading zero would be fine before the write, and real time forbids that. It's the pair of constraints together that leaves nothing.

@chapter One value flips it
@math heading="Change C to read 1" items="A B C:  w1, r→1 ✓, r→1 ✓@A B C;;A C B:  w1, r→1 ✓, r→1 ✓@A C B;;2 legal orders  →  linearizable@two legal"
Change C to read one, and nothing else. Same intervals, same constraint. Now A, B, C replays legally, and so does A, C, B. Two legal orders. The history is linearizable. One returned value flipped the verdict.

@words text="One copy, each operation at one instant"
That's what linearizability buys. The system behaves as if there were one copy of the data, and each operation took effect at a single instant between call and return. Quorum overlap only promised no acknowledged write is missed entirely.

@chapter Why it stops at six
@art factorial-wall
The growth is factorial. Six operations give seven hundred and twenty orders, the lab's cap. Seven give five thousand and forty, and the lab refuses, printing the number. Twenty give two point four times ten to the eighteen.

@art pruned-search
So real checkers don't enumerate. They search with pruning, commit operations greedily and backtrack, or check something weaker. The refusal is printed rather than silently truncated, because truncating would teach the opposite lesson.

@chapter Where people slip
@list heading="Common slips" items="Checking operations one at a time@The first|Reading overlap as permission for anything@The second|Expecting enumeration in practice@The third"
The first slip is checking operations one at a time. The second is reading overlapping intervals as permission to do anything. The verdict came from the forced pair. Look for those first. The third is expecting real checkers to enumerate.

@chapter Try it
@words text="A w1 [0,3] · B w2 [1,5] · C r1 [4,8] · D r2 [6,10]" sub="4! = 24 orders"
Your turn. Two concurrent writes and two reads. A writes one from zero to three, B writes two from one to five, C reads one from four to eight, D reads two from six to ten. Find the forced pairs, count the orders that survive real time, and say whether any are legal.

@end text="Enumerate a history yourself"
You can build a short history and watch every order filtered by real time and replay, on Learn. That's learn dot get er done dot I O.
