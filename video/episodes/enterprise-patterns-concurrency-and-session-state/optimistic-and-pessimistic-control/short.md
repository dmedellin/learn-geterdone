---
format: short
lesson: enterprise-patterns-concurrency-and-session-state/optimistic-and-pessimistic-control
title: Pessimistic locking isn't automatically safer
---

@art session-timeline
Is pessimistic locking safer? On one timeline, it only changes who pays.

@math items="optimistic: Martin redoes 10 minutes@ten minutes;;pessimistic: David kept out for 9@nine"
Two sessions edit one design. Optimistically, Martin's commit conflicts, and he redoes ten minutes. Pessimistically, David is refused at once, and kept out for nine.

@words text="No collision? Optimistic loses nothing."
Now take away Martin's commit. Pessimistically, David is still refused. Optimistically, he commits and nobody loses anything.

@end text="Full lesson on Learn"
The full lesson, with a lab that replays the timeline, is on Learn.
