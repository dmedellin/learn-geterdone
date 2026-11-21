---
format: short
lesson: enterprise-patterns-domain-logic/domain-model
title: Polymorphism doesn't remove decisions. It moves them
---

@art switch-routine
Replace a type switch with subclasses, and where do the decisions go?

@math items="one routine: 1 + if 3 + && 1 = 5@five decision points;;each kind its own rule: 1 + if 1 = 2@two"
One routine that prices books, alcohol and food has five decision points. Give each kind its own class, and the listing has two. Every price is unchanged.

@words text="Asked once, when the object is made"
The question, which kind is this, is now answered once, when you make a Book or a Food.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts them, is on Learn.
