---
format: short
lesson: enterprise-patterns-layers-and-performance/layer-supertype-and-separated-interface
title: Turn a dependency around with one interface
---

@art reversed-arrow
Your domain needs its mapper, but mustn't depend on it. Here's the trick.

@code block=1 lines=1-19 label=Java focus="2-4@interface|14@implements"
Define the interface in the domain package. Put the implementation, with the SQL, in the mapper package. It implements the interface, so now the mapper depends on the domain.

@math items="before: a jdbc change reaches 3@Before;;after: it reaches 2, no domain class@After"
Before, a change to jdbc reached three classes. After, it reaches two, and none of them is in the domain.

@end text="Full lesson on Learn"
The full lesson, with a lab that traces it, is on Learn.
