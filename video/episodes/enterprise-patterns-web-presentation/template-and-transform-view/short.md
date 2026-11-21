---
format: short
lesson: enterprise-patterns-web-presentation/template-and-transform-view
title: Can a template with no code show a condition?
---

@art helper-beside-page
If a page may hold no logic, how does it show anything conditional?

@words text="The helper decides. The marker asks."
Fowler's answer is a helper object. The helper holds the condition. The page holds a marker that asks it one true or false question.

@math items="ticket row, inline: 5@five decision points;;TicketHelper: isFew, showResale@isFew"
A ticket row with its decisions inline has five decision points. Move them into isFew and showResale, and the template holds none at all.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts them, is on Learn.
