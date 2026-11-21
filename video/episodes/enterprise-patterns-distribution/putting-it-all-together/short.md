---
format: short
lesson: enterprise-patterns-distribution/putting-it-all-together
title: Where you cut the layers changes everything
---

@art boundary-above-service
Same request, same layers. One cut costs nine remote calls. Another costs forty seven.

@math items="split above the Service Layer: 9 remote calls@above the service;;split under it: 47 remote calls@under it"
One request makes seventy four calls through the layers. Split the servers above the service, and nine cross the network. Split under it, and forty seven do, because the domain's fine calls cross.

@words text="Wrap the domain in a Remote Facade"
That's why Fowler says: one process if you can, and a Remote Facade if you can't.

@end text="Full lesson on Learn"
The full lesson, with a lab that prices each cut, is on Learn.
