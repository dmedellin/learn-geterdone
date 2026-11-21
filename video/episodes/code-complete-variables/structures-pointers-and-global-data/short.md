---
format: short
lesson: code-complete-variables/structures-pointers-and-global-data
title: A routine that only reads a global is still coupled
---

@art reader-coupled
This routine never writes a global. It's still coupled to three others.

@words text="Readers depend on every writer"
Because what it prints depends on what they wrote. Change one of the writers, and the reader's output changes too.

@art access-gate
Access routines don't remove that coupling. They put each global's representation in one place, so a change of representation is one edit.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the coupling, is on Learn.
