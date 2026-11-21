---
format: short
lesson: gof-creational/factory-method
title: The framework knows when, not which
---

@art app-document
A framework knows when to make a new document. It can't know which class.

@code block=1 lines=2-11 focus="3@an abstract operation|8@calls it"
So it declares an abstract operation that creates one, and calls it when it needs one.

@art parallel-hierarchies
Each subclass overrides it, and returns its own class. The framework never names a concrete product.

@words text="That's Factory Method"
That's Factory Method. The cost? Often a subclass just to make a product.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the classes, is on Learn.
