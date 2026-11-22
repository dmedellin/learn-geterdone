---
format: short
lesson: algorithmic-and-automated-trading/reliability-idempotency-retries-and-recovery
title: One order, three retries, four positions
---

@art four-orders
One timeout. Three retries. You might now hold four orders.

@math items="1 original + 3 retries = up to 4@one original"
If the submit times out after sending, the first order probably arrived. Retry three times with new IDs, and one original plus three retries is up to four orders.

@art idempotency-key
Reuse the same idempotency key on every attempt, and the broker sees one intent and holds one order.

@end text="Full lesson on Learn"
Inject timeouts and crashes in the full lesson on Learn.
