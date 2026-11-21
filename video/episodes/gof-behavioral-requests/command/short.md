---
format: short
lesson: gof-behavioral-requests/command
title: Why redo suddenly stops working
---

@art two-stacks
You undo twice, make one change, and redo stops working. Why?

@words text="Undo stack · redo stack"
Undo history is two stacks. Undo moves a command onto the redo stack. Redo moves it back.

@art discard-redo
But a new command empties the redo stack. Those undone changes belonged to a future that won't happen now. Redo them, and you'd apply them to the wrong state.

@end text="Full lesson on Learn"
That's the Command pattern. The full lesson is on Learn.
