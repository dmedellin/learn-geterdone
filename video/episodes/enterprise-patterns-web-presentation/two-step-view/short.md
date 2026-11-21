---
format: short
lesson: enterprise-patterns-web-presentation/two-step-view
title: Thirty view modules, or thirteen?
---

@art many-looks
Ten screens, three looks. Do you write thirty views, or thirteen?

@math items="single stage: 10 × 3 = 30@thirty;;two stages: 10 + 3 = 13@thirteen"
With a single stage view, each screen needs a view for each look: thirty. Split it into two stages, and you need ten first stages and three renderers: thirteen.

@art two-stages
The first stage builds a logical screen with no HTML. The second turns it into HTML, so a change of look is one change.

@end text="Full lesson on Learn"
The full lesson, with a lab that traces the change, is on Learn.
