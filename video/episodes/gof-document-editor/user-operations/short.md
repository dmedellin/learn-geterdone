---
format: short
lesson: gof-document-editor/user-operations
title: Why your redo disappears
---

@art history-line
You undo twice, then make one new edit. Where did your redo go?

@words text="Undo left · redo right"
Each request is a command object in a history, with a line marking the present. Undo steps left. Redo steps right.

@art redo-discarded
A new command replaces everything right of the line. In the lesson's garden controller, running summer discards the rain command that was waiting to be redone.

@end text="Full lesson on Learn"
The full lesson on Command, with a lab, is on Learn.
