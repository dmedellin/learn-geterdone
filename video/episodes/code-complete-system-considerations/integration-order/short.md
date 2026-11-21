---
format: short
lesson: code-complete-system-considerations/integration-order
title: Big bang integration, and why it fails
---

@art big-bang
Put every class together at once, and every bug shows up at once.

@words text="Big bang: any class is a suspect"
That's phased integration, and the book calls it big bang. When it breaks, any class could be the culprit, and nothing works until everything does.

@art skeleton-grow
Instead, start with a small working skeleton, and add one tested class at a time. When something breaks, you know where to look.

@end text="Full lesson on Learn"
The full lesson, with an integration order lab, is on Learn.
