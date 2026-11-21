---
format: short
lesson: enterprise-patterns-concurrency-and-session-state/transactions-and-isolation
title: Phantom or unrepeatable read? The stale item decides
---

@art isolation-ladder
Your report straddled a commit. Which isolation level would have stopped it?

@words text="Stale update → unrepeatable read" sub="read committed allows it · repeatable read prevents it"
Look at the item you read before the commit. If its change was an update, it's an unrepeatable read. Repeatable read prevents it.

@words text="Stale insert → phantom" sub="repeatable read allows it · serializable prevents it"
If every stale change was an insert, it's a phantom. Repeatable read lets that through, and only serializable stops it.

@end text="Full lesson on Learn"
The full lesson, with a lab that names the error, is on Learn.
