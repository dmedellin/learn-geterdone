---
format: short
lesson: algorithmic-and-automated-trading/broker-apis-and-order-lifecycle
title: Never retry an order with a new ID
---

@art client-order-id
Your order request times out. You retry with a fresh ID. Now you might own twice as much.

@words text="Timeout = unknown"
The broker may have accepted the first request before the response was lost.

@art timeout-unknown
So reuse the same client order ID, and query the broker. The same ID lets it recognise the retry as the order it already has.

@end text="Full lesson on Learn"
Inject timeouts in the full lesson on Learn.
