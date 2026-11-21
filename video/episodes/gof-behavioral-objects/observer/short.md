---
format: short
lesson: gof-behavioral-objects/observer
title: Four operations, twenty one updates
---

@art box-office
A theatre box office runs four operations. How many updates do its observers get?

@art broadcast
Every time a subject changes, it notifies every observer. Count it, and that's twenty one updates.

@art change-manager
Send them through a change manager that waits for each operation to finish, and it's thirteen.

@words text="Count before you subscribe"
One small change can reach a lot of objects. That's the warning built into Observer.

@end text="Full lesson on Learn"
The full lesson is on Learn.
