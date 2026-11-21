---
format: short
lesson: enterprise-patterns-concurrency-and-session-state/the-value-of-statelessness
title: A hundred users, ten objects
---

@art stateful-pinned
A hundred users can need a hundred server objects, or ten.

@math items="stateful: 100 objects, idle 90%@a hundred objects;;stateless: 100 × 1,000 / 10,000 = 10@ten"
Each user sends a one second request every ten seconds. Give each a stateful object, and that's a hundred objects, idle ninety percent of the time. Pool stateless ones, and ten do all the work.

@words text="The saving is the idle time"
Make users ask every two seconds, and you need fifty. The saving is the idle time.

@end text="Full lesson on Learn"
The full lesson, with a lab that does the arithmetic, is on Learn.
