---
format: short
lesson: gof-behavioral-objects/visitor
title: Should you use Visitor? One question decides
---

@art two-hierarchies
Will you add more operations, or more kinds of object? Visitor depends on the answer.

@art new-operation
With Visitor, a new operation is one new class, and nothing else changes.

@art new-kind
But a new kind of element changes every visitor you've written.

@words text="Operations change? Visitor." sub="Classes change? Keep operations in them."
So if your operations grow, use it. If your classes grow, keep the operations in the classes.

@end text="Full lesson on Learn"
The full lesson is on Learn.
