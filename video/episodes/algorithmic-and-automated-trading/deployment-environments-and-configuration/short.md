---
format: short
lesson: algorithmic-and-automated-trading/deployment-environments-and-configuration
title: The same bad deploy: 0.15% or 7%
---

@art canary-slice
One bad configuration. It costs you zero point one five percent, or seven.

@math items="10% × 0.5%/min × 3 min = 0.15%@ten percent canary;;100% × 0.5%/min × 14 min = 7%@full scope"
With a ten percent canary losing half a percent a minute and a three minute automatic rollback, the account loses zero point one five percent. At full scope with a fourteen minute manual rollback, seven.

@words text="Small canary, fast rollback"
Same bug.

@end text="Full lesson on Learn"
Inject a bad config in the full lesson on Learn.
