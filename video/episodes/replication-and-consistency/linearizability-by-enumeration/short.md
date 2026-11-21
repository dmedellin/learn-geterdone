---
format: short
lesson: replication-and-consistency/linearizability-by-enumeration
title: Every read returned a real value, and the system is still wrong
---

@art per-op-check
Every read here returned a value the register really held. It's still a violation.

@math items="A: write 1 [0,4] · B: read 1 [2,6] · C: read 0 [5,9]@A writes;;6 orders · 3 respect real time · 0 legal@Of six possible orders"
A writes one and finishes before C starts, so C must come after the write. But C read zero. Of six possible orders, three respect real time, and none of those replay legally.

@words text="Linearizability is about the whole history"
You can't check it one response at a time.

@end text="Full lesson on Learn"
The full lesson, with every order enumerated, is on Learn.
