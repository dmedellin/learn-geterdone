---
format: short
lesson: enterprise-patterns-distribution/plugin-and-service-stub
title: Why your unit test needs the network
---

@art ripple-direct
Change a network library, and your signup's unit test is affected. Why?

@math items="direct call: 3 reached, the test among them@three;;interface, stub, plugin at the edge: 2 reached@two"
If the signup calls the post office directly, a network change reaches three classes, the test among them. Put an interface between them, give the test a stub, and wire the real check in main. Now it reaches two, and neither is the test.

@words text="Choose the implementation at the edge"
One place, at startup, picks the stub or the real service.

@end text="Full lesson on Learn"
The full lesson, with a lab that traces the reach, is on Learn.
