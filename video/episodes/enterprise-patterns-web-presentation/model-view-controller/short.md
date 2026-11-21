---
format: short
lesson: enterprise-patterns-web-presentation/model-view-controller
title: Why your report breaks when you change HTML
---

@art ripple-reached
Change your HTML library, and a report with no HTML in it breaks. Why?

@math items="model knows html: 3 classes reached@three classes;;model knows nothing of pages: 1 reached@just one"
If the concert model formats itself with HTML, a change to that library reaches three classes, the report among them. Keep HTML out of the model, and it reaches just one: the page.

@words text="The page uses the model. Never the reverse."
That's Fowler's rule. The presentation depends on the model, and the model never depends on the presentation.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the reach, is on Learn.
