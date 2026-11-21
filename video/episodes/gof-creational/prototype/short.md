---
format: short
lesson: gof-creational/prototype
title: Why your copied object changed by itself
---

@art runners-template
Three runners copy one playlist template. One adds a track. Two others see it appear.

@art shallow-deep
That's a shallow copy. It shares every part it refers to, including the template's own list, so every later copy gets the track too.

@words text="Share only what cannot change"
A deep copy owns its parts. An immutable part is safe to share. As the Gang of Four put it, cloning forces you to decide what is shared.

@end text="Full lesson on Learn"
The full lesson on Prototype, with a lab, is on Learn.
