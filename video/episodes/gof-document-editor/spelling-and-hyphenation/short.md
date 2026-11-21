---
format: short
lesson: gof-document-editor/spelling-and-hyphenation
title: Add an analysis without touching a class
---

@art double-dispatch
Add a spelling checker to a document, without editing a single document class. Possible?

@words text="accept(visitor) → visitRecipe(this)"
Yes. Each part gets one accept operation, which calls back the visitor's method for its own class. A new analysis is just a new visitor.

@art eight-patterns
The catch: a new kind of part means editing every visitor. So ask which changes more often, the analyses or the parts.

@end text="Full lesson on Learn"
The full lesson, with Iterator and Visitor counted, is on Learn.
