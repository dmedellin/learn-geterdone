---
format: short
lesson: ddd-building-blocks/services
title: Why does a ticket know about refunds?
---

@words text="Why does a ticket know about refunds?"
Why would a theatre ticket hold a price list and a refunds account?

@art forced-operation
Because someone forced the exchange operation onto it. The ticket picked up dependencies it only needs for one job.

@art stateless-service
Evans's answer: sometimes it just isn't a thing. Make exchange a domain service, named for the activity, stateless, in the model's terms.

@end text="Full lesson on Learn"
Count where the dependencies go in the full lesson on Learn.
