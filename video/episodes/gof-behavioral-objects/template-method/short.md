---
format: short
lesson: gof-behavioral-objects/template-method
title: Don't call us, we'll call you
---

@art hollywood
In Template Method, the parent class calls the subclass. Never the other way round.

@art skeleton
The parent fixes the order of the steps. Subclasses must write the primitives, and may override the hooks.

@art missing-primitive
Forget a primitive, and the subclass is left abstract. The compiler catches it.

@words text="21 step bodies → 12"
Three map tile subclasses would write twenty one steps between them. With the template, it's twelve.

@end text="Full lesson on Learn"
The full lesson is on Learn.
