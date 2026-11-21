---
format: short
lesson: gof-behavioral-requests/memento
title: How does undo save state it can't see?
---

@art caretaker-shelf
How does an undo history save an object's state, without seeing inside it?

@art sealed-snapshot
The object makes a memento of itself, sealed. Only the object that made it can read it.

@art restore
The history just holds it, and hands it back on undo. The object restores itself.

@words text="15 values vs 1"
The cost? Full snapshots of a map view kept fifteen values, where inverse commands kept one.

@end text="Full lesson on Learn"
That's Memento. The full lesson is on Learn.
