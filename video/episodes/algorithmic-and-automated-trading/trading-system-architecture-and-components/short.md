---
format: short
lesson: algorithmic-and-automated-trading/trading-system-architecture-and-components
title: A timeout doesn't mean your order failed
---

@art safe-state
Your broker times out. Did the order fail? You don't know.

@words text="Timeout = unknown"
A timeout isn't proof the order failed. It might have filled. Retry blindly, and you can end up with two orders once the broker answers.

@words text="Enter a defined safe state"
So stop, enter a defined safe state, and reconcile with the broker before doing anything else.

@end text="Full lesson on Learn"
Inject failures and watch them in the full lesson on Learn.
