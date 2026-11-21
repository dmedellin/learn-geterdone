---
format: short
lesson: ddd-distillation/segregated-and-abstract-core
title: Slice your modules horizontally, not vertically
---

@art cycle-through-core
Modules by subdomain can leave every module depending on every other.

@quote text="Consider slicing horizontally rather than vertically." cite="Evans, Domain-Driven Design, Chapter 15"
Evans's advice: consider slicing horizontally rather than vertically.

@art arrows-inward
Put the domain's fundamental interfaces in one core module. In the lesson's bike share, that removes the cycle, and all five dependencies across the core's boundary point in. The core depends on none of them.

@end text="Full lesson on Learn"
Count the dependencies yourself in the full lesson on Learn.
