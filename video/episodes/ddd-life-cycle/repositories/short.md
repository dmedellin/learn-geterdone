---
format: short
lesson: ddd-life-cycle/repositories
title: Stop writing queries in your domain
---

@art query-leak
Every query a client writes pulls it out of the domain and into the database.

@art collection-illusion
Evans's repository is an illusion on purpose. Clients treat stored objects as if they were all in memory, add and remove them, and ask for the ones they want.

@words text="Only roots that need finding"
And only aggregate roots that can't be reached any other way get one.

@end text="Full lesson on Learn"
Ask a bike-share's repository in the full lesson on Learn.
