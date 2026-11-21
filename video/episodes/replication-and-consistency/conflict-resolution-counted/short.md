---
format: short
lesson: replication-and-consistency/conflict-resolution-counted
title: Perfect clocks won't stop last-writer-wins losing data
---

@art silent-drop
Four acknowledged increments, totalling ten. Last writer wins returns seven.

@math items="A +2 · B +3 · C +1 · B +4 = 10@Replica B;;LWW keeps B: 3 + 4 = 7@keeps"
Replica B holds the largest timestamp, so it keeps B's register, three plus four. A's two and C's one simply vanish, with no error raised anywhere.

@words text="Better clocks change who wins, not how many lose"
Exact clocks would only change which replica wins. A counter CRDT, merged by elementwise maximum, keeps all ten.

@end text="Full lesson on Learn"
The full lesson, with both merges counted, is on Learn.
