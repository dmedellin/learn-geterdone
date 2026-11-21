---
format: short
lesson: gof-introduction/what-is-a-design-pattern
title: Model View Controller is three patterns
---

@art mvc-three-views
That classic Model View Controller design? It's really three design patterns at once.

@list items="Observer@Observer|Composite@Composite|Strategy@Strategy"
The model tells its views when it changes: Observer. Views nest inside views: Composite. And each view hands its input to a swappable controller: Strategy.

@words text="A pattern is a shape, not a class"
That's the Gang of Four's point. A pattern is a recurring shape of objects, with a name and a cost.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the updates, is on Learn.
